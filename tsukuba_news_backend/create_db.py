import sqlite3
import csv
from collections import Counter

conn = sqlite3.connect("tsukuba_news.db")
c = conn.cursor()

# テーブル作成（pageカラムを追加）
c.execute('''
CREATE TABLE IF NOT EXISTS index_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    filename TEXT,
    page TEXT
)
''')

# まずfilenameごとの登場回数をカウント
with open("index.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    filename_list = [row['filename'] for row in reader]

filename_counter = Counter(filename_list)

# 20回を超えるfilenameはDBに入れない
with open("index.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if filename_counter[row['filename']] <= 20:
            c.execute(
                'INSERT INTO index_table (word, filename, page) VALUES (?, ?, ?)',
                (row['word'], row['filename'], row['page'])
            )

conn.commit()
conn.close()

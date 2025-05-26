import sqlite3
import csv

conn = sqlite3.connect("tsukuba_news.db")
c = conn.cursor()

# テーブル作成
c.execute('''
CREATE TABLE IF NOT EXISTS index_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT,
    filename TEXT
)
''')

# CSVから読み込み
with open("sample_data.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        c.execute('INSERT INTO index_table (word, filename) VALUES (?, ?)', (row['word'], row['filename']))

conn.commit()
conn.close()

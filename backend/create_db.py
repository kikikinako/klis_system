import sqlite3
import csv
from collections import Counter

conn = sqlite3.connect("tsukuba_news.db")
c = conn.cursor()

# テーブル作成(featureを追加)
c.execute('''
CREATE TABLE IF NOT EXISTS index_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT,
    title TEXT,
    url TEXT,
    issue TEXT,
    date TEXT,
    page TEXT,
    size TEXT,
    author TEXT
)
''')

# まずfilenameごとの登場回数をカウント
with open("index.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    title_list = [row['title'] for row in reader]

title_counter = Counter(title_list)

# 20回を超えるfilenameはDBに入れない
with open("index.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if title_counter[row['title']] <= 20:
            c.execute(
                'INSERT INTO index_table (keyword, title, url, issue, date, page, size, author) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (row['keyword'], row['title'], row['url'], row['issue'], row['date'], row['page'], row['size'], row['author'])
            )

conn.commit()
conn.close()

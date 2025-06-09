import sqlite3

conn = sqlite3.connect("tsukuba_news.db")
c = conn.cursor()

# テーブル作成
c.execute("SELECT * FROM index_table LIMIT 40")
rows = c.fetchall()

# データの表示
for row in rows:
    print(row)

conn.close()

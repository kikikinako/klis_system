import sqlite3

conn = sqlite3.connect("tsukuba_news.db")
c = conn.cursor()

# データの取得
c.execute('SELECT word, page FROM index_table WHERE word LIKE ?', ('%' + "筑波" + '%',))
rows = c.fetchall()

# データの表示
for row in rows:
    print(row)

conn.close()

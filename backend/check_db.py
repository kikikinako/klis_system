import sqlite3

conn = sqlite3.connect("tsukuba_news.db")
c = conn.cursor()

# データの取得
c.execute('SELECT title, url, issue, date, page, size, author FROM index_table WHERE keyword LIKE ?', ('%' + "12" + '%',))
rows = c.fetchall()

# データの表示
for row in rows:
    print(row)

conn.close()

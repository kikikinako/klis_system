import sqlite3

def print_table_preview(cursor, table_name):
    print(f"\n Preview of {table_name}:")
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = sqlite3.connect("tsukuba_news.db")
    c = conn.cursor()

    # 各テーブルの件数
    for table in ["index_table", "title_table"]:
        c.execute(f"SELECT COUNT(*) FROM {table}")
        count = c.fetchone()[0]
        print(f"{table} contains {count} rows.")

    # 各テーブルの中身を一部表示
    print_table_preview(c, "index_table")
    print_table_preview(c, "title_table")

    conn.close()

if __name__ == "__main__":
    main()

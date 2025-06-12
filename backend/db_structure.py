# db_structure.py
import sqlite3
import sys

def inspect_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # テーブル一覧を取得
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("❌ データベースにテーブルが存在しません。")
            return

        for table_name, in tables:
            print(f"\n📌 テーブル名: {table_name}")
            cursor.execute(f"PRAGMA table_info('{table_name}');")
            columns = cursor.fetchall()
            print("カラム情報:")
            print(f"{'cid':<5} {'name':<20} {'type':<15} {'notnull':<8} {'dflt_value':<15} {'pk':<5}")
            for col in columns:
                cid, name, col_type, notnull, dflt_value, pk = col
                print(f"{cid:<5} {name:<20} {col_type:<15} {notnull:<8} {str(dflt_value):<15} {pk:<5}")

    except sqlite3.Error as e:
        print(f"データベースエラー: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python db_structure.py <データベースファイル名>")
    else:
        inspect_db(sys.argv[1])

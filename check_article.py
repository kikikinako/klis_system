import sqlite3
import pandas as pd

# --- 設定 ---
DB_FILE_PATH = 'article.db'

# pandasの表示設定（コンソールでの表示を整える）
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 150) # 表示幅を広げる
pd.set_option('display.max_colwidth', 50)

def view_database_contents():
    """データベースに接続し、各テーブルの内容を表示する"""
    try:
        # データベースに接続
        conn = sqlite3.connect(DB_FILE_PATH)
        print(f"データベース '{DB_FILE_PATH}' に接続しました。\n")

        # 1. テーブル一覧の表示
        print("--- 1. テーブル一覧 ---")
        query_tables = "SELECT name FROM sqlite_master WHERE type='table';"
        tables_df = pd.read_sql_query(query_tables, conn)
        print(tables_df)
        print("\n" + "="*50 + "\n")

        # 2. 'articles' テーブルの内容表示 (先頭10件)
        print("--- 2. 'articles' テーブル (先頭10件) ---")
        query_articles = "SELECT * FROM articles LIMIT 10;"
        articles_df = pd.read_sql_query(query_articles, conn)
        print(articles_df)
        print("\n" + "="*50 + "\n")
        
        # 3. 'inverted_index' テーブルの内容表示 (先頭20件)
        print("--- 3. 'inverted_index' テーブル (先頭20件) ---")
        query_index = "SELECT * FROM inverted_index LIMIT 20;"
        index_df = pd.read_sql_query(query_index, conn)
        print(index_df)
        print("\n" + "="*50 + "\n")

        # 4. 検索デモ: '大学' という単語で検索
        print("--- 4. 検索デモ: 単語 '大学' で検索した結果 ---")
        search_term = "大学"
        
        # 【修正点】SELECTする列を新しいテーブル定義に合わせて全て取得する
        query_search = """
        SELECT
            T1.term,
            T2.title,
            T1.issue_number,
            T1.publication_date,
            T1.page,
            T1.size,
            T1.author
        FROM
            inverted_index AS T1
        JOIN
            articles AS T2 ON T1.article_id = T2.id
        WHERE
            T1.term = ?
        LIMIT 15;
        """
        # paramsでプレースホルダに値を安全に渡す
        search_df = pd.read_sql_query(query_search, conn, params=(search_term,))
        
        if search_df.empty:
            print(f"単語 '{search_term}' は見つかりませんでした。")
        else:
            print(search_df)
        print("\n" + "="*50 + "\n")

    except sqlite3.OperationalError as e:
        print(f"エラー: {e}")
        print(f"データベースファイル '{DB_FILE_PATH}' が見つからないか、テーブルが存在しない可能性があります。")
        print("先に `create_database.py` を実行してください。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")
    finally:
        # 接続が存在すれば必ず閉じる
        if 'conn' in locals() and conn:
            conn.close()
            print(f"データベース接続を閉じました。")

# --- 実行 ---
if __name__ == '__main__':
    view_database_contents()

from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
import ast

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/search', methods=['POST'])
def search_post():
    data = request.get_json()
    print(f"🔵 Received data: {data}")

    keyword = data.get('keywords', '')
    mode = data.get('mode', 'fulltext')  # 'title' または 'fulltext'

    if not keyword:
        return jsonify({"error": "No keyword provided"}), 400

    result = []

    if mode == "title":
        # 記事名検索: tsukuba_news_title.db → inverted_index → articles
        conn = sqlite3.connect("tsukuba_news_title.db")
        c = conn.cursor()

        # Step 1: term に該当する article_id を inverted_index から取得
        c.execute('''
            SELECT DISTINCT article_id
            FROM inverted_index
            WHERE term LIKE ?
        ''', ('%' + keyword + '%',))
        article_ids = [row[0] for row in c.fetchall()]

        # Step 2: article_id を使って articles テーブルから記事情報を取得
        if article_ids:
            placeholder = ','.join('?' for _ in article_ids)
            query = f'''
                SELECT title, issue_number, publication_date, page, size, author
                FROM articles
                WHERE id IN ({placeholder})
            '''
            c.execute(query, article_ids)
            rows = c.fetchall()

            for row in rows:
                result.append({
                    "title": row[0],
                    "issue": row[1],
                    "date": row[2],
                    "page": row[3], 
                    "size": row[4],
                    "author": row[5]
                })

        conn.close()

    elif mode == "fulltext":
        # 全文検索: tsukuba_news_fulltext.db の index_table
        conn = sqlite3.connect("tsukuba_news_fulltext.db")
        c = conn.cursor()

        # クエリを単語ごとに分割
        keywords = keyword.split()
        if not keywords:
            return jsonify([])

        # 各単語ごとに該当行を取得し、号・ページを集約
        tmp_result = {}
        for kw in keywords:
            c.execute('''
                SELECT filename, page
                FROM index_table
                WHERE word LIKE ?
            ''', ('%' + kw + '%',))
            rows = c.fetchall()
            for row in rows:
                filenames = ast.literal_eval(row[0])
                page_lists = ast.literal_eval(row[1])
                for n in range(len(filenames)):
                    filename = filenames[n]
                    page_list = page_lists[n]
                    if filename in tmp_result:
                        tmp_result[filename] += page_list
                    else:
                        tmp_result[filename] = page_list

        for key in tmp_result:
            tmp_result[key] = sorted(set(tmp_result[key])) #重複の除去とソート
            result.append({
                "filename": key,
                "page": tmp_result[key]
            })

        conn.close()

    else:
        return jsonify({"error": "Invalid search mode"}), 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

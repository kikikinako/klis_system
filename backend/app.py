from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/search', methods=['POST'])
def search_post():
    data = request.get_json()
    print(f"🔵 Received data: {data}")

    keyword = data.get('keywords', '')
    mode = data.get('mode', 'fulltext')  # 'fulltext' または 'title'

    if not keyword:
        return jsonify({"error": "No keyword provided"}), 400

    conn = sqlite3.connect("tsukuba_news.db")
    c = conn.cursor()
    result = []

    if mode == "fulltext":
        # 全文検索：inverted_index から article_id を検索
        c.execute('''
            SELECT DISTINCT article_id 
            FROM inverted_index 
            WHERE term LIKE ?
        ''', ('%' + keyword + '%',))
        article_ids = [str(row[0]) for row in c.fetchall()]

        if not article_ids:
            conn.close()
            return jsonify([])

        # article_id に該当する記事情報を articles テーブルから取得
        placeholders = ','.join(['?'] * len(article_ids))
        query = f'''
            SELECT id, title, issue_number, publication_date, page, size, author
            FROM articles
            WHERE id IN ({placeholders})
        '''
        c.execute(query, article_ids)
        articles = c.fetchall()

    elif mode == "title":
        # 記事名検索：title カラムで部分一致検索
        c.execute('''
            SELECT id, title, issue_number, publication_date, page, size, author
            FROM articles
            WHERE title LIKE ?
        ''', ('%' + keyword + '%',))
        articles = c.fetchall()

    else:
        conn.close()
        return jsonify({"error": "Invalid search mode"}), 400

    # 出力フォーマットを統一（両方とも articles テーブルからの取得なので同じ構造）
    for row in articles:
        result.append({
            "id": row[0],
            "title": row[1],
            "issue": row[2],
            "date": row[3],
            "page": row[4],
            "size": row[5],
            "author": row[6]
        })

    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

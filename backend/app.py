from flask import Flask, request, jsonify
import sqlite3
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # フロントと連携のため

@app.route('/search', methods=['POST'])
def search_post():
    data = request.get_json()  # フロントエンドから送られたJSONを受け取る
    print(f"🔵 Received data: {data}") # debug
    keyword = data.get('keywords', '')  # React側で "keywords" というキーを使って送る

    if not keyword:
        return jsonify({"error": "No keyword provided"}), 400

    # SQLiteデータベースに接続
    conn = sqlite3.connect("tsukuba_news.db")
    c = conn.cursor()
    c.execute('SELECT filename, page FROM index_table WHERE word LIKE ?', ('%' + keyword + '%',))
    row = c.fetchone()
    conn.close()

    if row:
        filenames = json.loads(row[0])
        pages = json.loads(row[1])
        return jsonify({"filename": filenames, "page": pages})
    else:
        return jsonify({"filename": [], "page": []})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
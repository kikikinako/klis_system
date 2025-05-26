from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # フロントと連携のため

@app.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"error": "No keyword provided"}), 400

    conn = sqlite3.connect("tsukuba_news.db")
    c = conn.cursor()
    c.execute('SELECT DISTINCT filename FROM index_table WHERE word LIKE ?', ('%' + keyword + '%',))
    results = c.fetchall()
    conn.close()

    return jsonify([r[0] for r in results])

if __name__ == "__main__":
    app.run(debug=True)

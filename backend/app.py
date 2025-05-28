from flask import Flask, request, jsonify
from flask_cors import CORS
import search

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def result():
    data = request.get_json()
    keywords = data["keywords"]
    sort = data["sort"]
    result = search.search(keywords, sort)
    
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8000)
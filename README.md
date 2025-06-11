# klis_system
## 接続テスト方法

1. バックエンドを起動

cd tsukuba_news_backend
python app.py

→ http://localhost:8000 で Flask が起動します。

2. フロントエンドを起動

cd frontend
npm install   # 初回のみ
npm run dev

→ http://localhost:5173 をブラウザで開きます。

3. テスト手順

- 入力欄にキーワード（例：「筑波」）を入力
- 「Submit form」ボタンをクリック
- 結果が表示されます
- Flask 側にもリクエストログが表示されれば接続成功です

import requests
import json

# FlaskサーバーのURL
URL = "http://localhost:8000/search"

# 検索キーワードとモードを切り替えてテスト
test_cases = [
    {"keywords": "筑波", "mode": "title"},
    {"keywords": "筑波", "mode": "fulltext"}
]

for test in test_cases:
    print(f"\n🔍 Testing with: {test}")
    try:
        response = requests.post(URL, json=test)
        if response.status_code == 200:
            result = response.json()
            print("✅ Response:")
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"⚠️ Exception occurred: {e}")

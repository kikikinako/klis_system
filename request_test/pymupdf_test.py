import fitz  # PyMuPDF
import re
from janome.tokenizer import Tokenizer
import os 

index = {}
t = Tokenizer()

pattern = re.compile(r"[　-ー]$")
num_pattern = re.compile(r"[^\u3040-\u30FF\u4E00-\u9FFFa-zA-Z\s]")


for number in range(247,388):
    # PDFファイルを開く
    doc = fitz.open(f"pdfs/{number}.pdf")
    # 全ページのテキストを結合
    all_text = ""
    for page in doc:
        all_text += page.get_text()
    doc.close()
    # 空白・改行・タブを削除（日本語のように単語区切りが不要な言語に適応）
    clean_text = all_text.replace(" ", "").replace("\n", "").replace("\t", "")
    
    tokens = t.tokenize(clean_text)
    
    for token in tokens:
        word = token.surface.lower()
        if pattern.match(word):
            continue
        if num_pattern.match(word):
            continue
        if len(word) <= 1:  # 1文字以下を除外
            continue
        if word in index:
            if number not in index[word]:
                index[word].append(number)
        else:
            index[word] = [number]
        
with open('index.txt', 'w', encoding='utf-8') as f:
    for words in sorted(index):
        f.write(f"{words}: {index[words]}\n")
    
    
    
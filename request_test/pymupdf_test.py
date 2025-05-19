import fitz  # PyMuPDF
import re
from janome.tokenizer import Tokenizer
import os 

index = {}
t = Tokenizer()

pattern = re.compile(r"[　-ー]$")
num_pattern = re.compile(r"[^\u3040-\u30FF\u4E00-\u9FFFa-zA-Z]")


for number in range(300,388):
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
        if pattern.match(token.surface):
            continue
        if num_pattern.match(token.surface):
            continue
        if token.surface in index:
            if number not in index[token.surface]:
                index[token.surface].append(number)
        else:
            index[token.surface] = [number]
        
print(index)
    
    
    
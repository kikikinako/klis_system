import fitz  # PyMuPDF
import re

index = {}

for number in range(212,388):
    # PDFファイルを開く
    doc = fitz.open(f"pdfs/{number}.pdf")
    # 全ページのテキストを結合
    all_text = ""
    for page in doc:
        all_text += page.get_text()
    doc.close()
    # 空白・改行・タブを削除（日本語のように単語区切りが不要な言語に適応）
    clean_text = all_text.replace(" ", "").replace("\n", "").replace("\t", "")
    
    
    
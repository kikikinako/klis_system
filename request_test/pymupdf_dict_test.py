import fitz  # PyMuPDF
import re
from janome.tokenizer import Tokenizer
import os 

index = {}
t = Tokenizer()



# ...existing code...
for number in range(387,388):
    doc = fitz.open(f"pdfs/{number}.pdf")
    titles = []
    for page_num, page in enumerate(doc, start=1):
        text_dict = page.get_text("dict")
        for block in text_dict["blocks"]:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span["size"] >= 20:  # フォントサイズ9以上のみ抽出
                            print(f"ページ: {page_num}, テキスト: {span['text']}, フォントサイズ: {span['size']}")
    doc.close()
# ...existing code...
    # 空白・改行・タブを削除（日本語のように単語区切りが不要な言語に適応）


    
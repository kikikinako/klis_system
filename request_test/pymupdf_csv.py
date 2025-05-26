import fitz  # PyMuPDF
import re
from janome.tokenizer import Tokenizer
import os
import csv

index = {}
t = Tokenizer()

pattern = re.compile(r"[　-ー]$")
num_pattern = re.compile(r"[^\u3040-\u30FF\u4E00-\u9FFFa-zA-Z\s]")

# index: {単語: {号番号: set(ページ番号)}}
for number in range(247, 388):
    doc = fitz.open(f"pdfs/{number}.pdf")
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        clean_text = text.replace(" ", "").replace("\n", "").replace("\t", "")
        tokens = t.tokenize(clean_text)
        for token in tokens:
            word = token.surface.lower()
            if pattern.match(word):
                continue
            if num_pattern.match(word):
                continue
            if len(word) <= 1:
                continue
            if word not in index:
                index[word] = {}
            if number not in index[word]:
                index[word][number] = set()
            index[word][number].add(page_num)
    doc.close()

with open('index.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['単語', '号番号リスト', 'ページ番号リスト'])
    for word in sorted(index):
        num_list = sorted(index[word].keys())
        page_list = [sorted(list(index[word][num])) for num in num_list]
        writer.writerow([
            word,
            str(num_list),
            str(page_list)
        ])
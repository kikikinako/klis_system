import requests
from bs4 import BeautifulSoup
import os
import re
import fitz  # PyMuPDF

url = "https://www.tsukuba.ac.jp/about/public-newspaper/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

pdf_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.endswith(".pdf"):
        filename = href.split("/")[-1]
        if re.fullmatch(r"\d+\.pdf", filename):  
            href = "https://www.tsukuba.ac.jp/about/public-newspaper/" + href
            pdf_links.append(href)

for pdf_url in pdf_links:
    response = requests.get(pdf_url)
    filename = pdf_url[-7:-4] + ".pdf"  # Extract the last 6 characters before .pdf
    with open(os.path.join("pdfs", filename), "wb") as f:
                f.write(response.content)

import os
import requests
from readability import Document
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# URLs to scrape
URLS = [
    "https://en.wikipedia.org/wiki/Tirupati",
    "https://en.wikipedia.org/wiki/Varanasi",
    "https://en.wikipedia.org/wiki/Kedarnath_Temple",
    "https://en.wikipedia.org/wiki/Venkateswara_Temple,_Tirumala",
    "https://en.wikipedia.org/wiki/Badrinath_Temple",
    "https://en.wikipedia.org/wiki/Sai_Baba_Temple,_Shirdi",
    ""
    
]

os.makedirs("data", exist_ok=True)

def extract_text(html):
    doc = Document(html)
    soup = BeautifulSoup(doc.summary(), "html.parser")
    for tag in soup(["script", "style", "table", "aside"]):
        tag.decompose()
    return doc.title(), soup.get_text("\n", strip=True)

def save_pdf(text, path):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    y = height - 40
    for line in text.split("\n"):
        c.drawString(40, y, line[:100])  # simple width control
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40
    c.save()

for i, url in enumerate(URLS, 1):
    print("Processing:", url)
    res = requests.get(url)
    title, text = extract_text(res.text)
    save_pdf(title + "\n\n" + text, f"data/doc_{i}.pdf")

print("Done.")

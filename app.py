import json
from bs4 import BeautifulSoup

with open("sample.xml", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "xml")

news_list = []

for entry in soup.find_all("entry"):
    title_tag = entry.find("title")
    link_tag = entry.find("link")
    summary_tag = entry.find("summary")
    content_tag = entry.find("content")

    title = title_tag.get_text(strip=True) if title_tag else None
    link = link_tag.get("href") if link_tag else None

    text = None
    if content_tag:
        text = content_tag.get_text(strip=True)
    elif summary_tag:
        text = summary_tag.get_text(strip=True)

    news_list.append({
        "title": title,
        "link": link,
        "text": text
    })

with open("sample.json", "w", encoding="utf-8") as f:
    json.dump(news_list, f, ensure_ascii=False, indent=4)
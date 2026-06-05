import requests
from bs4 import BeautifulSoup

def get_article_text(url):

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join(
            p.get_text(strip=True)
            for p in paragraphs
        )

        return text[:2000]

    except Exception:
        return ""

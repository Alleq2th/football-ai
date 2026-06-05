from flask import Flask
from news_fetcher import get_news

app = Flask(__name__)

@app.route("/")
def home():
    news = get_news()

    return {
        "name": "Football AI",
        "status": "running",
        "stories_found": len(news),
        "news": news[:5]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

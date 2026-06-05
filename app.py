from flask import Flask
from news_fetcher import get_news
from content_generator import generate_content

app = Flask(__name__)

@app.route("/")
def home():

    news = get_news()

    posts = []

    for story in news[:5]:

        content = generate_content(story["title"])

        posts.append({
            "headline": story["title"],
            "link": story["link"],
            "content": content
        })

    return {
        "name": "Football AI",
        "status": "running",
        "posts_generated": len(posts),
        "posts": posts
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

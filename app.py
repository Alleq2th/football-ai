from flask import Flask, render_template
from news_fetcher import get_news
from content_generator import generate_content
from story_ranker import score_story

app = Flask(__name__)

@app.route("/")
def home():

    news = get_news()
    
    news.sort(
    key=lambda story: score_story(story["title"]),
    reverse=True
    )

    posts = []

    for story in news[:20]:

        content = generate_content(story["title"])

        posts.append({
    "headline": story["title"],
    "link": story["link"],
    "score": score_story(story["title"]),
    "content": content
})
        })

    return render_template(
        "index.html",
        posts=posts
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

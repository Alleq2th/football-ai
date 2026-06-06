from flask import Flask, render_template, send_file
from news_fetcher import get_news
from content_generator import generate_content
from story_ranker import score_story
from graphic_generator import create_graphic

app = Flask(__name__)

@app.route("/")
def home():

    news = get_news()

    news = sorted(
        news,
        key=lambda story: score_story(story["title"]),
        reverse=True
    )

    posts = []

    for story in news[:5]:

        content = generate_content(
            story["title"],
            story["link"]
        )

        posts.append({
            "headline": story["title"],
            "link": story["link"],
            "score": score_story(story["title"]),
            "content": content
        })

    return render_template(
        "index.html",
        posts=posts
    )

@app.route("/generate_graphic/<path:headline>")
def generate_graphic(headline):

    filename = create_graphic(headline)

    return send_file(
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

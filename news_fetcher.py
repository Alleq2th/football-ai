import feedparser

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/sport/football/rss.xml",
    "https://www.espn.com/espn/rss/soccer/news"
]

def get_news():
    all_news = []

    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:10]:
                all_news.append({
                    "title": entry.title,
                    "link": entry.link
                })

        except Exception:
            pass

    return all_news

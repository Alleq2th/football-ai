def generate_content(headline):
    
    news_post = f"""
🚨 FOOTBALL UPDATE

{headline}

Stay tuned for more football news.
"""

    engagement_post = f"""
👀 Football fans...

{headline}

What's your opinion on this?
Drop your thoughts below.
"""

    instagram_post = f"""
⚽🔥 {headline}

Football never stops delivering drama.

What do you think?

#football #soccer #premierleague
"""

    return {
        "news_post": news_post.strip(),
        "engagement_post": engagement_post.strip(),
        "instagram_post": instagram_post.strip()
    }

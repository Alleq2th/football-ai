import random
from story_classifier import classify_story
from article_reader import get_article_text

def generate_content(headline, link):

    story_type = classify_story(headline)

    article_text = get_article_text(link)

    if article_text:
        summary = article_text[:300]
    else:
        summary = headline

    if story_type == "world_cup":

        news_post = f"""🌍 WORLD CUP UPDATE

{headline}

📰 Summary:
{summary}

⚡ Why It Matters:
• This could affect World Cup preparations.
• Teams and fans will be watching closely.
• Tournament expectations may change.

💬 Question:
How important is this story for the World Cup?
"""

    elif story_type == "transfer":

        news_post = f"""🔄 TRANSFER UPDATE

{headline}

📰 Summary:
{summary}

⚡ Why It Matters:
• It could change a team's season.
• Fans will debate whether it's a good move.
• Rival clubs may respond.

💬 Question:
Would you make this signing?
"""

    elif story_type == "manager":

        news_post = f"""👔 MANAGER UPDATE

{headline}

📰 Summary:
{summary}

⚡ Why It Matters:
• Coaching decisions shape results.
• Squad morale may be affected.
• Fans will judge the decision quickly.

💬 Question:
Was this the right decision?
"""

    elif story_type == "champions_league":

        news_post = f"""🏆 CHAMPIONS LEAGUE

{headline}

📰 Summary:
{summary}

⚡ Why It Matters:
• Champions League matches define seasons.
• Pressure increases for players and managers.
• Qualification and trophies are on the line.

💬 Question:
How will this impact the competition?
"""

    else:

        news_post = f"""⚽ FOOTBALL UPDATE

{headline}

📰 Summary:
{summary}

⚡ Why It Matters:
• This could influence upcoming matches.
• Fans are discussing the implications.
• Clubs may need to react.

💬 Question:
What's your opinion on this story?
"""

    engagement_templates = [
        f"🔥 {headline}\n\nWhat do you think?",
        f"👀 {headline}\n\nAgree or disagree?",
        f"⚽ {headline}\n\nFootball fans, thoughts?"
    ]

    instagram_templates = [
        f"⚽ {headline}\n\n#Football #FootballNews",
        f"🔥 {headline}\n\n#Soccer #Football",
        f"👀 {headline}\n\n#FootballNews"
    ]

    return {
        "news_post": news_post,
        "engagement_post": random.choice(engagement_templates),
        "instagram_post": random.choice(instagram_templates)
    }

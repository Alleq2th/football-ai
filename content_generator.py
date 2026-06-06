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

    engagement_post = f"""🔥 {headline}

{summary}

This story could have a significant impact on football fans, players, and teams depending on how events develop in the coming days. Discussions are already beginning across the football world, and many supporters will have strong opinions on what happens next.

What is your take on this situation? Do you agree with the decisions being made, or would you do things differently?
"""

    instagram_post = f"""⚽ {headline}

{summary}

Football never stops delivering big talking points, and this is another story that could shape conversations among fans. Whether you're supporting the player, manager, or club involved, there is plenty to discuss as more details emerge.

👇 Share your thoughts below.

#Football #FootballNews #Soccer #WorldCup #ChampionsLeague
"""

    return {
        "news_post": news_post,
        "engagement_post": engagement_post,
        "instagram_post": instagram_post
        }

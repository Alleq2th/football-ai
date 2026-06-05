import random

def generate_content(headline):

    news_templates = [
        f"🚨 BREAKING\n\n{headline}\n\nMore details to follow.",
        f"⚽ FOOTBALL UPDATE\n\n{headline}\n\nStay tuned for more.",
        f"📢 LATEST NEWS\n\n{headline}\n\nFootball never sleeps."
    ]

    debate_templates = [
        f"👀 Football fans...\n\n{headline}\n\nWhat's your opinion?",
        f"🤔 Be honest...\n\n{headline}\n\nAre people overreacting or not?",
        f"🔥 Hot take:\n\n{headline}\n\nAgree or disagree?"
    ]

    instagram_templates = [
        f"⚽🔥 {headline}\n\nRate this from 1–10 👇\n\n#football #soccer",
        f"👀 {headline}\n\nThoughts?\n\n#football #premierleague",
        f"🔥 Football never disappoints.\n\n{headline}\n\n#footballnews"
    ]

    return {
        "news_post": random.choice(news_templates),
        "engagement_post": random.choice(debate_templates),
        "instagram_post": random.choice(instagram_templates)
    }

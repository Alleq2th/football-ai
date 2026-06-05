import random
from story_classifier import classify_story

def generate_content(headline):

    story_type = classify_story(headline)

    if story_type == "world_cup":

        return {
            "news_post":
                f"🌍 WORLD CUP UPDATE\n\n{headline}\n\nThis could have a major impact on the tournament.",

            "engagement_post":
                f"🌍 World Cup fans...\n\n{headline}\n\nHow big of a deal is this?",

            "instagram_post":
                f"🌍 {headline}\n\nCould this affect the World Cup in a major way?\n\n#WorldCup #Football"
        }

    elif story_type == "transfer":

        return {
            "news_post":
                f"🔄 TRANSFER UPDATE\n\n{headline}",

            "engagement_post":
                f"👀 Transfer Talk\n\n{headline}\n\nSmart signing or bad business?",

            "instagram_post":
                f"🔄 {headline}\n\nRate this move from 1-10.\n\n#TransferNews #Football"
        }

    elif story_type == "manager":

        return {
            "news_post":
                f"👔 MANAGER UPDATE\n\n{headline}",

            "engagement_post":
                f"🤔 Manager Debate\n\n{headline}\n\nRight decision or mistake?",

            "instagram_post":
                f"👔 {headline}\n\nWhat happens next?\n\n#Football"
        }

    elif story_type == "champions_league":

        return {
            "news_post":
                f"🏆 CHAMPIONS LEAGUE\n\n{headline}",

            "engagement_post":
                f"🏆 UCL Debate\n\n{headline}\n\nWho benefits most from this?",

            "instagram_post":
                f"🏆 {headline}\n\nChampions League drama never stops.\n\n#UCL #ChampionsLeague"
        }

    else:

        news_templates = [
            f"🚨 BREAKING\n\n{headline}",
            f"⚽ FOOTBALL UPDATE\n\n{headline}",
            f"📢 LATEST NEWS\n\n{headline}"
        ]

        engagement_templates = [
            f"👀 Football fans...\n\n{headline}\n\nWhat's your opinion?",
            f"🔥 Hot take:\n\n{headline}\n\nAgree or disagree?",
            f"🤔 Be honest...\n\n{headline}\n\nThoughts?"
        ]

        instagram_templates = [
            f"⚽ {headline}\n\n#Football",
            f"🔥 {headline}\n\n#FootballNews",
            f"👀 {headline}\n\n#Soccer"
        ]

        return {
            "news_post": random.choice(news_templates),
            "engagement_post": random.choice(engagement_templates),
            "instagram_post": random.choice(instagram_templates)
        }

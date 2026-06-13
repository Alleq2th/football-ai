"""
Content Style Database

Controls how content is written
for different creator personalities.
"""

CONTENT_STYLES = {

    "Aggressive": {
        "tone": "Bold and direct",
        "hook_style": "Controversial",
        "emoji_level": "Low"
    },

    "Funny": {
        "tone": "Humorous",
        "hook_style": "Entertaining",
        "emoji_level": "High"
    },

    "Educational": {
        "tone": "Teaching",
        "hook_style": "Value First",
        "emoji_level": "Low"
    },

    "Storytelling": {
        "tone": "Narrative",
        "hook_style": "Curiosity",
        "emoji_level": "Medium"
    },

    "Analytical": {
        "tone": "Data Driven",
        "hook_style": "Insight",
        "emoji_level": "Low"
    },

    "Debate": {
        "tone": "Argumentative",
        "hook_style": "Hot Take",
        "emoji_level": "Medium"
    },

    "Reporter": {
        "tone": "News Style",
        "hook_style": "Breaking News",
        "emoji_level": "Low"
    },

    "Motivational": {
        "tone": "Inspirational",
        "hook_style": "Challenge",
        "emoji_level": "Medium"
    },

    "Luxury": {
        "tone": "Premium",
        "hook_style": "Status",
        "emoji_level": "Low"
    },

    "Sarcastic": {
        "tone": "Witty",
        "hook_style": "Mocking",
        "emoji_level": "Medium"
    }
}


def get_styles():

    return list(CONTENT_STYLES.keys())


def get_style(style_name):

    return CONTENT_STYLES.get(style_name)


def style_exists(style_name):

    return style_name in CONTENT_STYLES


if __name__ == "__main__":

    print("AVAILABLE STYLES")
    print(get_styles())

    print("\nFUNNY STYLE")
    print(get_style("Funny"))

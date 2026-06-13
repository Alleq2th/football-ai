"""
Master Niche Database

This file contains all main niches and sub niches
used throughout the Creator Operating System.
"""

NICHES = {

    "Sports": [
        "Football",
        "Basketball",
        "UFC",
        "Boxing",
        "Formula 1",
        "Tennis",
        "Cricket",
        "Golf",
        "NFL",
        "Rugby",
        "Baseball",
        "Athletics"
    ],

    "Technology": [
        "Artificial Intelligence",
        "Cybersecurity",
        "Programming",
        "Startups",
        "Tech News",
        "Apple",
        "Android",
        "Software Reviews",
        "Hardware Reviews"
    ],

    "Finance": [
        "Personal Finance",
        "Investing",
        "Stocks",
        "Crypto",
        "Real Estate",
        "Side Hustles",
        "Business News",
        "Entrepreneurship"
    ],

    "Gaming": [
        "Fortnite",
        "Call Of Duty",
        "FIFA",
        "EA FC",
        "Minecraft",
        "Roblox",
        "Valorant",
        "League Of Legends",
        "GTA",
        "Gaming News"
    ],

    "Entertainment": [
        "Movies",
        "TV Shows",
        "Celebrity News",
        "Music",
        "Pop Culture",
        "Awards Shows"
    ],

    "Streaming": [
        "Twitch",
        "Kick",
        "YouTube Streaming",
        "Streamer Drama",
        "Kai Cenat",
        "IShowSpeed",
        "VTubers"
    ],

    "Religion": [
        "Christianity",
        "Islam",
        "Bible Teaching",
        "Motivational Faith",
        "Prayer Content"
    ],

    "Education": [
        "Science",
        "History",
        "Geography",
        "Mathematics",
        "Language Learning"
    ],

    "Health": [
        "Fitness",
        "Weight Loss",
        "Bodybuilding",
        "Nutrition",
        "Mental Health"
    ],

    "Lifestyle": [
        "Fashion",
        "Luxury",
        "Travel",
        "Food",
        "Relationships",
        "Parenting"
    ]
}


def get_main_niches():
    """
    Returns all main niches.
    """

    return list(NICHES.keys())


def get_sub_niches(main_niche):
    """
    Returns sub niches
    for a specific main niche.
    """

    return NICHES.get(main_niche, [])


def niche_exists(main_niche):
    """
    Check if niche exists.
    """

    return main_niche in NICHES


if __name__ == "__main__":

    print("MAIN NICHES")
    print(get_main_niches())

    print("\nSPORTS SUB NICHES")
    print(get_sub_niches("Sports"))

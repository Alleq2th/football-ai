"""
Platform Database

Stores all supported platforms
and content formats.
"""

PLATFORMS = {

    "TikTok": [
        "Short Video",
        "Photo Post",
        "Story"
    ],

    "Instagram": [
        "Reels",
        "Carousel",
        "Image Post",
        "Stories"
    ],

    "Facebook": [
        "Reels",
        "Posts",
        "Stories",
        "Groups"
    ],

    "YouTube": [
        "Shorts",
        "Long Form",
        "Community Posts"
    ],

    "X": [
        "Posts",
        "Threads"
    ],

    "LinkedIn": [
        "Posts",
        "Articles"
    ],

    "Reddit": [
        "Posts",
        "Comments"
    ],

    "Pinterest": [
        "Pins",
        "Boards"
    ],

    "Threads": [
        "Threads Posts"
    ],

    "Telegram": [
        "Channel Posts"
    ],

    "WhatsApp": [
        "Channel Posts"
    ],

    "Discord": [
        "Server Posts"
    ],

    "Snapchat": [
        "Spotlight"
    ],

    "Twitch": [
        "Streams"
    ],

    "Kick": [
        "Streams"
    ],

    "Medium": [
        "Articles"
    ],

    "Blog": [
        "Blog Posts"
    ]
}


def get_platforms():

    return list(PLATFORMS.keys())


def get_formats(platform):

    return PLATFORMS.get(platform, [])


def platform_exists(platform):

    return platform in PLATFORMS


if __name__ == "__main__":

    print("SUPPORTED PLATFORMS")
    print(get_platforms())

    print("\nINSTAGRAM FORMATS")
    print(get_formats("Instagram"))

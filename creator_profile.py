"""
Creator Profile Model

Stores creator information
used throughout the platform.
"""


class CreatorProfile:

    def __init__(
        self,
        name,
        followers,
        main_niche,
        sub_niche,
        platforms,
        content_style,
        posts_per_day
    ):

        self.name = name

        self.followers = followers

        self.main_niche = main_niche

        self.sub_niche = sub_niche

        self.platforms = platforms

        self.content_style = content_style

        self.posts_per_day = posts_per_day

    def to_dict(self):

        return {

            "name": self.name,

            "followers": self.followers,

            "main_niche": self.main_niche,

            "sub_niche": self.sub_niche,

            "platforms": self.platforms,

            "content_style": self.content_style,

            "posts_per_day": self.posts_per_day

        }

    def summary(self):

        return f"""
Creator: {self.name}
Followers: {self.followers}
Main Niche: {self.main_niche}
Sub Niche: {self.sub_niche}
Platforms: {', '.join(self.platforms)}
Style: {self.content_style}
Posts Per Day: {self.posts_per_day}
"""


if __name__ == "__main__":

    creator = CreatorProfile(

        name="Greg",

        followers=1200,

        main_niche="Sports",

        sub_niche="Football",

        platforms=[
            "TikTok",
            "Instagram",
            "YouTube"
        ],

        content_style="Aggressive",

        posts_per_day=5

    )

    print(creator.summary())

"""
Analytics Engine V1

Responsible for:

- Tracking content performance
- Calculating engagement
- Calculating virality score
- Identifying winning content
"""

class AnalyticsEngine:

    def __init__(self):

        self.posts = []

    def add_post(

        self,
        title,
        platform,
        views,
        likes,
        comments,
        shares

    ):

        engagement = (

            likes +
            comments +
            shares

        )

        virality_score = (

            engagement / max(views, 1)

        ) * 100

        post = {

            "title": title,

            "platform": platform,

            "views": views,

            "likes": likes,

            "comments": comments,

            "shares": shares,

            "engagement": engagement,

            "virality_score": round(
                virality_score,
                2
            )

        }

        self.posts.append(post)

        return post

    def get_top_posts(

        self,
        limit=10

    ):

        return sorted(

            self.posts,

            key=lambda x: x["virality_score"],

            reverse=True

        )[:limit]

    def get_average_views(self):

        if not self.posts:

            return 0

        total = sum(

            post["views"]

            for post in self.posts

        )

        return round(

            total / len(self.posts),

            2

        )

    def get_average_engagement(self):

        if not self.posts:

            return 0

        total = sum(

            post["engagement"]

            for post in self.posts

        )

        return round(

            total / len(self.posts),

            2

        )

    def get_best_topics(self):

        winners = self.get_top_posts(5)

        return [

            post["title"]

            for post in winners

        ]


if __name__ == "__main__":

    analytics = AnalyticsEngine()

    analytics.add_post(

        title="World Cup Final",

        platform="TikTok",

        views=50000,

        likes=7000,

        comments=900,

        shares=1500

    )

    analytics.add_post(

        title="Transfer News",

        platform="Instagram",

        views=30000,

        likes=2500,

        comments=300,

        shares=400

    )

    print(

        analytics.get_top_posts()

    )

    print(

        analytics.get_best_topics()

      )

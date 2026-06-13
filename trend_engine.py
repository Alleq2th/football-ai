"""
Trend Engine V1

Responsible for:

- Trend collection
- Trend scoring
- Trend filtering
- Platform matching
- Niche matching

Future Versions:

- Google Trends
- Reddit Trends
- TikTok Trends
- X Trends
- Instagram Trends
- YouTube Trends
- Event Calendar Integration
"""


from datetime import datetime


class Trend:

    def __init__(
        self,
        title,
        source,
        niche,
        platform,
        score=50
    ):

        self.title = title

        self.source = source

        self.niche = niche

        self.platform = platform

        self.score = score

        self.created_at = datetime.now()

    def to_dict(self):

        return {

            "title": self.title,

            "source": self.source,

            "niche": self.niche,

            "platform": self.platform,

            "score": self.score,

            "created_at": str(self.created_at)

        }


class TrendEngine:

    def __init__(self):

        self.trends = []

    def add_trend(

        self,
        title,
        source,
        niche,
        platform,
        score=50

    ):

        trend = Trend(

            title=title,
            source=source,
            niche=niche,
            platform=platform,
            score=score

        )

        self.trends.append(trend)

        return trend

    def get_all_trends(self):

        return [

            trend.to_dict()

            for trend in self.trends

        ]

    def get_trends_by_niche(

        self,
        niche

    ):

        return [

            trend.to_dict()

            for trend in self.trends

            if trend.niche.lower()
            == niche.lower()

        ]

    def get_trends_by_platform(

        self,
        platform

    ):

        return [

            trend.to_dict()

            for trend in self.trends

            if trend.platform.lower()
            == platform.lower()

        ]

    def get_top_trends(

        self,
        limit=10

    ):

        sorted_trends = sorted(

            self.trends,

            key=lambda x: x.score,

            reverse=True

        )

        return [

            trend.to_dict()

            for trend in sorted_trends[:limit]

        ]

    def score_trend(

        self,
        title

    ):

        title = title.lower()

        score = 50

        viral_keywords = [

            "viral",
            "breaking",
            "shocking",
            "leaked",
            "controversy",
            "exposed",
            "drama",
            "final",
            "winner",
            "announcement"

        ]

        for keyword in viral_keywords:

            if keyword in title:

                score += 10

        return min(score, 100)


if __name__ == "__main__":

    engine = TrendEngine()

    engine.add_trend(

        title="Breaking World Cup News",

        source="Google News",

        niche="Sports",

        platform="TikTok",

        score=95

    )

    engine.add_trend(

        title="New AI Tool Goes Viral",

        source="Reddit",

        niche="Technology",

        platform="Instagram",

        score=88

    )

    print(

        engine.get_top_trends()

      )

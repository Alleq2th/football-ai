"""
Image Engine V1

Responsible for:

- Image prompt generation
- Thumbnail prompt generation
- Carousel generation prompts
- Social media graphic prompts
"""

class ImageEngine:

    def __init__(self):

        pass

    def generate_image_prompt(

        self,
        trend,
        niche,
        platform

    ):

        return f"""
Create a professional {platform} graphic.

Topic:
{trend}

Niche:
{niche}

Style:
Modern, viral, high engagement.

Include:
Bold headline
Strong focal point
Professional composition
Social-media optimized
"""

    def generate_thumbnail_prompt(

        self,
        trend

    ):

        return f"""
Create a high CTR YouTube thumbnail.

Topic:
{trend}

Requirements:

Large text
Strong emotions
Bright contrast
Professional sports/news style
"""

    def generate_carousel_prompt(

        self,
        trend

    ):

        slides = []

        for i in range(1, 6):

            slides.append(

                f"Slide {i}: {trend}"

            )

        return slides

    def generate_tiktok_cover(

        self,
        trend

    ):

        return {

            "headline": trend,

            "style": "viral",

            "format": "9:16"

        }


if __name__ == "__main__":

    engine = ImageEngine()

    print(

        engine.generate_image_prompt(

            trend="World Cup Final",

            niche="Sports",

            platform="Instagram"

        )

  )

"""
Script Engine V1

Responsible for:

- Script generation
- Hook generation
- Platform adaptation
- Content style adaptation
"""

import random


class ScriptEngine:

    def __init__(self):

        pass

    def generate_hook(

        self,
        trend,
        style

    ):

        hooks = {

            "Aggressive": [

                f"Nobody is talking about this: {trend}",

                f"This changes everything in {trend}",

                f"Stop scrolling. You need to hear this."

            ],

            "Funny": [

                f"This is actually hilarious 😂",

                f"I can't believe this happened.",

                f"The internet is losing its mind."

            ],

            "Educational": [

                f"Here's what you need to know.",

                f"Let's break this down simply.",

                f"Most people misunderstand this."

            ],

            "Storytelling": [

                f"It started with one small mistake.",

                f"Nobody expected this to happen.",

                f"This story gets crazy fast."

            ]

        }

        style_hooks = hooks.get(

            style,

            hooks["Educational"]

        )

        return random.choice(style_hooks)

    def generate_script(

        self,
        trend,
        style,
        platform

    ):

        hook = self.generate_hook(

            trend,
            style

        )

        if platform == "TikTok":

            return {

                "hook": hook,

                "body": f"Today we're talking about {trend}. Here's why everyone is paying attention right now.",

                "cta": "Follow for more updates."

            }

        elif platform == "Instagram":

            return {

                "hook": hook,

                "body": f"{trend} is trending right now. Here's what you need to know.",

                "cta": "Save this post and share it."

            }

        elif platform == "YouTube":

            return {

                "hook": hook,

                "body": f"In today's video we explore {trend} and what it means going forward.",

                "cta": "Subscribe for more content."
            }

        else:

            return {

                "hook": hook,

                "body": f"{trend} is currently trending.",

                "cta": "Follow for more."
            }


if __name__ == "__main__":

    engine = ScriptEngine()

    result = engine.generate_script(

        trend="World Cup Final",

        style="Aggressive",

        platform="TikTok"

    )

    print(result)

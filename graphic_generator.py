from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def create_graphic(headline):

    headline_lower = headline.lower()

    # Default Theme
    bg_color = (10, 15, 35)
    header_color = (0, 102, 255)
    banner_color = (220, 30, 30)
    logo_path = None
    banner_text = "BREAKING NEWS"

    # World Cup
    if "world cup" in headline_lower:
        bg_color = (8, 24, 64)
        header_color = (196, 160, 40)
        banner_color = (196, 160, 40)
        logo_path = "assets/competition_logos/world_cup.png"
        banner_text = "WORLD CUP"

    # Champions League
    elif "champions league" in headline_lower:
        bg_color = (5, 20, 80)
        header_color = (255, 255, 255)
        banner_color = (25, 50, 150)
        logo_path = "assets/competition_logos/champions_league.png"
        banner_text = "CHAMPIONS LEAGUE"

    # Premier League
    elif "premier league" in headline_lower:
        bg_color = (55, 0, 90)
        header_color = (120, 0, 180)
        banner_color = (0, 255, 180)
        logo_path = "assets/competition_logos/premier_league.png"
        banner_text = "PREMIER LEAGUE"

    width = 1080
    height = 1080

    # Create Gradient Background
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    for y in range(height):

        ratio = y / height

        r = int(bg_color[0] * (1 - ratio * 0.5))
        g = int(bg_color[1] * (1 - ratio * 0.5))
        b = int(bg_color[2] * (1 - ratio * 0.5))

        draw.line(
            [(0, y), (width, y)],
            fill=(r, g, b)
        )

    draw = ImageDraw.Draw(image)

    # Fonts
    title_font = ImageFont.truetype(
        "fonts/Anton-Regular.ttf",
        120
    )

    banner_font = ImageFont.truetype(
        "fonts/Anton-Regular.ttf",
        60
    )

    footer_font = ImageFont.truetype(
        "fonts/Anton-Regular.ttf",
        38
    )

    small_font = ImageFont.truetype(
        "fonts/Anton-Regular.ttf",
        30
    )

    # Header
    draw.rectangle(
        [(0, 0), (1080, 120)],
        fill=header_color
    )

    draw.text(
        (40, 25),
        "FOOTBALL AI NEWSROOM",
        font=banner_font,
        fill=(255, 255, 255)
    )

    # Date
    today = datetime.now().strftime("%d %b %Y")

    draw.text(
        (820, 40),
        today,
        font=small_font,
        fill=(255, 255, 255)
    )

    # Category Banner
    draw.rounded_rectangle(
        [(40, 170), (650, 260)],
        radius=20,
        fill=banner_color
    )

    draw.text(
        (70, 185),
        banner_text,
        font=banner_font,
        fill=(255, 255, 255)
    )

    # Top Story Badge
    draw.rounded_rectangle(
        [(60, 290), (280, 345)],
        radius=18,
        fill=(255, 255, 255)
    )

    draw.text(
        (95, 300),
        "TOP STORY",
        font=small_font,
        fill=(0, 0, 0)
    )

    # Logo Circle
    draw.ellipse(
        [(780, 110), (1040, 370)],
        fill=(255, 255, 255)
    )

    # Competition Logo
    if logo_path:
        try:

            logo = Image.open(
                logo_path
            ).convert("RGBA")

            logo.thumbnail((180, 180))

            image.paste(
                logo,
                (820, 150),
                logo
            )

        except:
            pass

    # Headline Formatting
    words = headline.upper().split()

    lines = []
    current = ""

    for word in words:

        if len(current + " " + word) <= 14:
            current += " " + word

        else:
            lines.append(current.strip())
            current = word

    lines.append(current)

    y = 390

    for line in lines[:4]:

        # Shadow
        draw.text(
            (66, y + 6),
            line,
            font=title_font,
            fill=(0, 0, 0)
        )

        # Main Text
        draw.text(
            (60, y),
            line,
            font=title_font,
            fill=(255, 255, 255)
        )

        y += 130

    # Divider Line
    draw.line(
        [(60, 900), (1020, 900)],
        fill=(255, 255, 255),
        width=4
    )

    # Watermark
    draw.text(
        (760, 960),
        "@FootballAI",
        font=footer_font,
        fill=(80, 80, 80)
    )

    filename = "static/latest_graphic.png"

    image.save(filename)

    return filename

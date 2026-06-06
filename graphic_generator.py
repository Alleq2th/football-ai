from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime

def create_graphic(headline):

    headline_lower = headline.lower()

    bg_top = (10, 20, 50)
    bg_bottom = (3, 8, 20)
    accent = (220, 30, 30)

    logo_path = None
    banner_text = "BREAKING"

    if "world cup" in headline_lower:
        bg_top = (10, 30, 90)
        bg_bottom = (2, 8, 30)
        accent = (196, 160, 40)
        logo_path = "assets/world_cup.png"
        banner_text = "WORLD CUP"

    elif "champions league" in headline_lower:
        bg_top = (10, 35, 120)
        bg_bottom = (0, 10, 40)
        accent = (255, 255, 255)
        logo_path = "assets/champions_league.png"
        banner_text = "CHAMPIONS LEAGUE"

    elif "premier league" in headline_lower:
        bg_top = (70, 0, 120)
        bg_bottom = (20, 0, 40)
        accent = (0, 255, 180)
        logo_path = "assets/premier_league.png"
        banner_text = "PREMIER LEAGUE"

    width = 1080
    height = 1080

    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    for y in range(height):
        ratio = y / height
        r = int(bg_top[0] * (1 - ratio) + bg_bottom[0] * ratio)
        g = int(bg_top[1] * (1 - ratio) + bg_bottom[1] * ratio)
        b = int(bg_top[2] * (1 - ratio) + bg_bottom[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([(620, 80), (1040, 500)], fill=(255, 255, 255, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(120))

    image = Image.alpha_composite(image.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(image)

    try:
        headline_length = len(headline)

        if headline_length < 40:
            title_size = 88
        elif headline_length < 70:
            title_size = 78
        else:
            title_size = 68

        title_font = ImageFont.truetype("fonts/Anton-Regular.ttf", title_size)
        banner_font = ImageFont.truetype("fonts/Anton-Regular.ttf", 52)
        small_font = ImageFont.truetype("fonts/Anton-Regular.ttf", 30)
        watermark_font = ImageFont.truetype("fonts/Anton-Regular.ttf", 42)

    except:
        title_font = ImageFont.load_default()
        banner_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        watermark_font = ImageFont.load_default()

    if logo_path:
        try:
            bg_logo = Image.open(logo_path).convert("RGBA")
            bg_logo.thumbnail((550, 550))

            alpha = bg_logo.split()[3]
            alpha = alpha.point(lambda p: int(p * 0.08))
            bg_logo.putalpha(alpha)

            image.paste(bg_logo, (260, 260), bg_logo)
        except:
            pass

    draw.rectangle([(0, 0), (1080, 90)], fill=accent)

    draw.text((40, 12), "FOOTBALL AI NEWSROOM",
              font=banner_font, fill="white")

    today = datetime.now().strftime("%d %b %Y")

    draw.text((820, 28), today,
              font=small_font, fill="white")

    draw.rounded_rectangle(
        [(50, 140), (650, 220)],
        radius=20,
        fill=accent
    )

    draw.text(
        (80, 152),
        banner_text,
        font=banner_font,
        fill="white"
    )

    draw.rounded_rectangle(
        [(60, 255), (250, 310)],
        radius=15,
        fill=(255, 255, 255)
    )

    draw.text(
        (88, 266),
        "TOP STORY",
        font=small_font,
        fill=(0, 0, 0)
    )

    score = min(99, max(70, 100 - (len(headline) // 2)))

    draw.rounded_rectangle(
        [(270, 255), (390, 310)],
        radius=15,
        fill=accent
    )

    draw.text(
        (290, 266),
        str(score),
        font=small_font,
        fill="white"
    )

    draw.ellipse(
        [(800, 120), (990, 310)],
        fill=(196, 160, 40)
    )

    draw.ellipse(
        [(808, 128), (982, 302)],
        fill=(255, 255, 255)
    )

    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((155, 155))
            image.paste(logo, (817, 137), logo)
        except:
            pass

    draw.rounded_rectangle(
        [(35, 340), (780, 820)],
        radius=30,
        fill=(20, 20, 20)
    )

    words = headline.upper().split()
    lines = []
    current = ""

    for word in words:
        test = (current + " " + word).strip()
        if len(test) <= 16:
            current = test
        else:
            lines.append(current)
            current = word

    if current:
        lines.append(current)

    y = 380

    for line in lines[:4]:
        draw.text((66, y + 6), line, font=title_font, fill=(0, 0, 0))
        draw.text((60, y), line, font=title_font, fill=(255, 255, 255))
        y += 95

    draw.line([(60, 900), (1020, 900)], fill=(255, 255, 255), width=3)

    draw.text(
        (520, 945),
        "FOOTBALL AI • @FootballAI",
        font=watermark_font,
        fill=(70, 70, 70)
    )

    filename = "static/latest_graphic.png"
    image.save(filename)
    return filename
        

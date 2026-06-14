‎from PIL import Image, ImageDraw, ImageFont, ImageFilter
‎from datetime import datetime
‎
‎def create_graphic(headline):
‎
‎    headline_lower = headline.lower()
‎
‎    # DEFAULT THEME
‎    bg_top = (10, 20, 50)
‎    bg_bottom = (3, 8, 20)
‎    accent = (220, 30, 30)
‎
‎    logo_path = None
‎    banner_text = "BREAKING"
‎
‎    # WORLD CUP
‎    if "world cup" in headline_lower:
‎        bg_top = (10, 30, 90)
‎        bg_bottom = (2, 8, 30)
‎        accent = (196, 160, 40)
‎        logo_path = "assets/world_cup.png"
‎        banner_text = "WORLD CUP"
‎
‎    # CHAMPIONS LEAGUE
‎    elif "champions league" in headline_lower:
‎        bg_top = (10, 35, 120)
‎        bg_bottom = (0, 10, 40)
‎        accent = (255, 255, 255)
‎        logo_path = "assets/champions_league.png"
‎        banner_text = "CHAMPIONS LEAGUE"
‎
‎    # PREMIER LEAGUE
‎    elif "premier league" in headline_lower:
‎        bg_top = (70, 0, 120)
‎        bg_bottom = (20, 0, 40)
‎        accent = (0, 255, 180)
‎        logo_path = "assets/premier_league.png"
‎        banner_text = "PREMIER LEAGUE"
‎
‎    width = 1080
‎    height = 1080
‎
‎    image = Image.new("RGB", (width, height))
‎    draw = ImageDraw.Draw(image)
‎
‎    # PREMIUM GRADIENT
‎    for y in range(height):
‎
‎        ratio = y / height
‎
‎        r = int(bg_top[0] * (1 - ratio) + bg_bottom[0] * ratio)
‎        g = int(bg_top[1] * (1 - ratio) + bg_bottom[1] * ratio)
‎        b = int(bg_top[2] * (1 - ratio) + bg_bottom[2] * ratio)
‎
‎        draw.line(
‎            [(0, y), (width, y)],
‎            fill=(r, g, b)
‎        )
‎
‎    # GLOW EFFECT
‎    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
‎    glow_draw = ImageDraw.Draw(glow)
‎
‎    glow_draw.ellipse(
‎        [(650, 120), (1050, 520)],
‎        fill=(255, 255, 255, 35)
‎    )
‎
‎    glow = glow.filter(ImageFilter.GaussianBlur(120))
‎
‎    image = Image.alpha_composite(
‎        image.convert("RGBA"),
‎        glow
‎    ).convert("RGB")
‎
‎    draw = ImageDraw.Draw(image)
‎
‎    try:
‎        title_font = ImageFont.truetype(
‎            "fonts/Anton-Regular.ttf",
‎            88
‎        )
‎
‎        banner_font = ImageFont.truetype(
‎            "fonts/Anton-Regular.ttf",
‎            52
‎        )
‎
‎        small_font = ImageFont.truetype(
‎            "fonts/Anton-Regular.ttf",
‎            30
‎        )
‎
‎        watermark_font = ImageFont.truetype(
‎            "fonts/Anton-Regular.ttf",
‎            48
‎        )
‎
‎    except:
‎        title_font = ImageFont.load_default()
‎        banner_font = ImageFont.load_default()
‎        small_font = ImageFont.load_default()
‎        watermark_font = ImageFont.load_default()
‎
‎    # HEADER
‎    draw.rectangle(
‎        [(0, 0), (1080, 110)],
‎        fill=accent
‎    )
‎
‎    draw.text(
‎        (40, 18),
‎        "FOOTBALL AI NEWSROOM",
‎        font=banner_font,
‎        fill="white"
‎    )
‎
‎    today = datetime.now().strftime("%d %b %Y")
‎
‎    draw.text(
‎        (820, 32),
‎        today,
‎        font=small_font,
‎        fill="white"
‎    )
‎
‎    # CATEGORY BAR
‎    draw.rounded_rectangle(
‎        [(50, 160), (650, 240)],
‎        radius=20,
‎        fill=accent
‎    )
‎
‎    draw.text(
‎        (80, 172),
‎        banner_text,
‎        font=banner_font,
‎        fill="white"
‎    )
‎
‎    # TOP STORY
‎    draw.rounded_rectangle(
‎        [(60, 275), (250, 330)],
‎        radius=15,
‎        fill=(255, 255, 255)
‎    )
‎
‎    draw.text(
‎        (88, 286),
‎        "TOP STORY",
‎        font=small_font,
‎        fill=(0, 0, 0)
‎    )
‎
‎    # SCORE BADGE
‎    draw.rounded_rectangle(
‎        [(270, 275), (390, 330)],
‎        radius=15,
‎        fill=accent
‎    )
‎
‎    draw.text(
‎        (305, 286),
‎        "95",
‎        font=small_font,
‎        fill="white"
‎    )
‎
‎    # LOGO CIRCLE
‎    draw.ellipse(
‎        [(790, 120), (1010, 340)],
‎        fill=(255, 255, 255)
‎    )
‎
‎    if logo_path:
‎
‎        try:
‎
‎            logo = Image.open(
‎                logo_path
‎            ).convert("RGBA")
‎
‎            logo.thumbnail((140, 140))
‎
‎            image.paste(
‎                logo,
‎                (830, 160),
‎                logo
‎            )
‎
‎        except:
‎            pass
‎
‎    # HEADLINE WRAPPING
‎    words = headline.upper().split()
‎
‎    lines = []
‎    current = ""
‎
‎    for word in words:
‎
‎        test_line = current + " " + word
‎
‎        if len(test_line) <= 16:
‎            current = test_line.strip()
‎
‎        else:
‎            lines.append(current)
‎            current = word
‎
‎    if current:
‎        lines.append(current)
‎
‎    y = 390
‎
‎    for line in lines[:4]:
‎
‎        draw.text(
‎            (66, y + 6),
‎            line,
‎            font=title_font,
‎            fill=(0, 0, 0)
‎        )
‎
‎        draw.text(
‎            (60, y),
‎            line,
‎            font=title_font,
‎            fill=(255, 255, 255)
‎        )
‎
‎        y += 105
‎
‎    # DIVIDER
‎    draw.line(
‎        [(60, 900), (1020, 900)],
‎        fill=(255, 255, 255),
‎        width=3
‎    )
‎
‎    # WATERMARK
‎    draw.text(
‎        (700, 945),
‎        "@FootballAI",
‎        font=watermark_font,
‎        fill=(90, 90, 90)
‎    )
‎
‎    filename = "static/latest_graphic.png"
‎
‎    image.save(filename)
‎
‎    return filename
‎

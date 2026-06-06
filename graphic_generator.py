from PIL import Image, ImageDraw, ImageFont

def create_graphic(headline):

    width = 1080
    height = 1080

    image = Image.new("RGB", (width, height), (10, 15, 35))

    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype(
            "fonts/Anton-Regular.ttf",
            90
        )
    except:
        title_font = ImageFont.load_default()

    draw.text(
        (60, 200),
        headline[:60],
        fill=(255, 255, 255),
        font=title_font
    )

    filename = "static/latest_graphic.png"

    image.save(filename)

    return filename

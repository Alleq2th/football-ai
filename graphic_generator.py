from PIL import Image, ImageDraw

def create_graphic(headline):

    width = 1080
    height = 1080

    image = Image.new("RGB", (width, height), (15, 15, 15))

    draw = ImageDraw.Draw(image)

    draw.text(
        (50, 80),
        "⚽ FOOTBALL AI",
        fill=(255, 255, 255)
    )

    draw.text(
        (50, 250),
        headline[:100],
        fill=(255, 255, 255)
    )

    filename = "static/latest_graphic.png"

    image.save(filename)

    return filename

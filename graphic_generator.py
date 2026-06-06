from PIL import Image, ImageDraw

def create_graphic(headline):

    width = 1080
    height = 1080

    image = Image.new("RGB", (width, height), (20, 20, 20))

    draw = ImageDraw.Draw(image)

    draw.text(
        (60, 120),
        "FOOTBALL AI",
        fill=(255, 255, 255)
    )

    draw.text(
        (60, 300),
        headline[:80],
        fill=(255, 255, 255)
    )

    filename = "static/latest_graphic.png"

    image.save(filename)

    return filename

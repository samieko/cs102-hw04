import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size()

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

# TODO: Replace this with your own filter!

for x in width:
    for y in height:
        r, g, b = img.getpixel((x, y))
        new_color = (r, g, b)
        for z in new_color:
            if r < 150:
                r = 199
            else:
                r = 230
            if g > 100:
                g = 80
            else:
                g = 90
            if b < 100:
                b = 106
            else:
                b = 106
        new_img.putpixel((x, y), (r, g, b))

# i was attempting to tint the input image red, but i think i made an error somewhere.

new_img.save(output_path, "JPEG")

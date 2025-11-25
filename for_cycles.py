from PIL import Image

# Про библиотеку Pillow можно почитать тут:
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class
# и, скажем, тут: https://habr.com/ru/articles/681248/


im = Image.open("images/cant_sleep.jpg")
print(f'image size {im.size}')

# box = (0, 0, 1000, 1000)
# region = im.crop(box)
# region.show()

# ВНИМАНИЕ! В Pillow первой координатой идет X!
for x in range(im.size[0] // 2):
    for y in range(im.size[1] // 2):
        pix = im.getpixel((x, y))
        avg = (pix[0] + pix[1] + pix[2]) //3
        im.putpixel((x, y), (avg, avg, avg))

im.show()
im.save('./cant_sleep2.jpg')
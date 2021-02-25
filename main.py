import sys
from PIL import Image
from PIL import ImageFont, ImageDraw

# get image
image_path = "portal.jpg"
img = Image.open(image_path)

# resize image
width, height = img.size
aspect_ratio = height / width

#calculate new hight
new_width = 120
new_height = aspect_ratio * new_width

img = img.resize((new_width, int(new_height)))

# convert each pixel to grayscale
img = img.convert('L')
#img.save("new_image.jpg")

# get each grayscale pixel
chars = list(reversed( ["P","S","#","&","@","$","%","*","!",":","."]))

pixels = img.getdata()

new_pixels = [chars[pixel // 25 ] for pixel in pixels]
new_pixels = ''.join(new_pixels)

new_pixels_count = len(new_pixels)

#final image
ascii_image = [new_pixels [index:index + new_width] for index in range (0, new_pixels_count, new_width)]

ascii_image = "\n".join(ascii_image)
print(ascii_image)

with open("ascii_image.txt", "w") as file:
  file.write(ascii_image)




#print(img.size)
#img.show()
# calculate aspect ratio

# resize
#I managed to save pic to jpg
im = Image.new("RGB", (width*20, height*20), (256,256,256))

# get a font
font = ImageFont.truetype("FreeMono.ttf", 40)

# get a drawing context
d = ImageDraw.Draw(im)

# draw multiline text
d.multiline_text((0, 0), ascii_img_out, font=font, fill=(0, 0, 0))

# save Image
im.save("new_img.jpg")
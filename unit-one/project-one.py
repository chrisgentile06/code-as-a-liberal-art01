## First I need to Open images

# from os import listdir, path
# import random
# from PIL import Image

# files = listdir("images")
# # files.remove(".DS_Store")

# random_file = random.choice(files)

# img = Image.open( path.join("images",random_file) )

# img.save("my-random-piece.png")
# # print(img)


## Then I want to isolate images like the filtered images we made + put pixel array over images

# # FILTER PIXELS AS A LIST

# img = Image.open( sys.argv[1] )
# img_hsv = img.convert(mode="HSV")
# img_hsv_data = img_hsv.getdata()

# new_img_data = []
# for p in img_hsv_data:
#     print(p)
#     if p[2] < 55:
#         new_img_data.append( (255,255,255) )
#     else:
#         new_img_data.append(p)


# img_hsv.putdata(new_img_data)
# img_rgb = img_hsv.convert("RGB")
# img_rgb.save("filtered.jpg")


## RANDOM DOTS


# width = 100
# height = 100

# img = Image.new("HSV", (width,height), (0,0,0) )

# for y in range(height):
#     for x in range(width):    
#         # randomColorValue = random.randrange(255)
    
#         r = random.random()

#         if r > .9:
#             img.putpixel( (x,y), (240,255,255) )

# img = img.convert("RGB")

# randomnumberforimage = int(random.random() * 1000 )

# img.save("so-less-random" + str(randomnumberforimage) + ".png")




## I ALSO want to put number markers on random pixels in images, random coordinates outlines on the image

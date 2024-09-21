import sys
from PIL import Image

#making the different images...
if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img1 = Image.new("RGB", (400,400) )
#     for y in range(400)
#         for x in range(400):

#         r = 0
#         b = 0
#         if x % 30 == 0:
#             b = 555
            
#         if y % 60 == 0:
#             r = 355

#         if y % 30 == 0:
#             r = 355
#             b = 5555

#         pixel = (r, 0, b)
#         img.putpixel( (x,y), pixel )
### Above makes the stringy plaid..

# Make a new 400x400 image
# img = Image.new("RGB", (400,400) )


# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         g = 0
#         b = 0
#         if x % 60 > 25:
#             r = 300

#         if y % 40 > 25:
#             b = 255

#         if x % 80 > 50 and y % 80 > 50:
#             g = 800

#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])
## (x% 60 . 25) r = 300 (y % 40>25) b = 255 (x % 80 > 50 and y % 80 > 50) g = 800 gives back small yellow and green cubes, slimmer blue lines, and thicker red ones...
#tester2

# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         g = 0
#         b = 0
#         if x % 26 > 25:
#             r = 100

#         if y % 90 > 25:
#             b = 600

#         if x % 80 > 50 and y % 80 > 50:
#             g = 500

#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1]) 
## tester3

# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         g = 0
#         b = 0
#         if x % 150 > 25:
#             r = 800

#         if y % 40 > 25:
#             b = 255

#         if x % 120 > 50 and y % 120 > 50:
#             g = 800

#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])
#tester4

img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        g = 0
        b = 0
        if x % 150 > 25:
            r = 800

        if y % 40 > 25:
            b = 15

        if x % 150 > 50 and y % 150 > 50:
            g = 900

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])
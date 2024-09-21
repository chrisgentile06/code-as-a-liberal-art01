import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This program requires two arguments: the name of two image files to combine.")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )


img1.thumbnail( (400,400) )
img2.thumbnail( (400,400) )

# make a new image 600x600, with a white background
# Note that this image now has an "alpha" component
new_image = Image.new( "RGBA", (400,400), "white" )


new_image.paste(img1, (0,0) )


img1.putalpha(180)


new_image.alpha_composite(img1, (0,0) )

new_image.convert("RGB").save("overlay-transparent3.jpg")

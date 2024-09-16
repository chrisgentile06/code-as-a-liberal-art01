import sys
from PIL import Image

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

# print("You typed the filename: " + sys.argv[1] )
# print("This is a " + img.format)
# print(img.format_description)
# print("Size: " + str(img.size) )

# rotated_img = img.rotate( int(sys.argv[2]) )
# rotated_img.save("rotated-" + sys.argv[1]) 
#successfully rotated image-1 once i added the degree after image title...

blended_img = Image.blend(img1,img2,.5)
blended_img.save("blended.jpg")
#photos need to be made the sam size or error occurs.
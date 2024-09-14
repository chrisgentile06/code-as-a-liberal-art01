#import sys

#print( sys.argv)

#print(len(sys.argv))

#index = int(sys.argv[1]) will only identify numbers.

import sys
from PIL import Image

img = Image.open( sys.argv[1] )

print("You typed the filename: " + sys.argv[1] )
print("This is a " + img.format)
print(img.format_description)
print("Size: " + str(img.size) )
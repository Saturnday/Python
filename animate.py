
"""
import sys
from PIL import Image

images = []

#arg = sys.argv[1:] don't need to write this line
for arg in sys.argv[1:]: #straight away write the arg in the sys.argv
   image=Image.open(arg)#pass the arg to the function in PIL to open the image
   images.append(image) 

images[0].save(
   "images.gif", save_all=True, append_images=[images[1:]], duration=200, loop=0
)
#don't forgot to type a name of the new file 
#save_all should be passed with True
#the the append_images should be passed the argument of the list
#don't use timeout, instead use duration
#it's better to start in new line for this ammount of arguments
"""
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
   image = Image.open(arg) 
   images.append(image) 

images[0].save(
   "images.gif", save_all=True, append_images=images[1:], duration=200, loop=0, disposal=2
)

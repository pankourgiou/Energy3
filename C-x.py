from matplotlib import pyplot as plt 
import numpy as np
from PIL import Image
im=Image.open("A_View_from_the_Top_of_the_World.jpg")
pxl=list(im.getdata())
print ("pxl")
columnsize,rowsize=im.size

a = np.array(pxl)
plt.hist(a, bins = 255)
plt.title("histogram") 
plt.show()

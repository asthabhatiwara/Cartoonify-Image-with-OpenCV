import cv2
import numpy as np 

import sys
import matplotlib.pyplot as plt  # for plotting and visualization of images 

import easygui  # open the filebox and return the file name



def upload():
      Image=easygui.fileopenbox()
      cartoonify(Image)
     

#Cartoonizer effect  
#A class that applies a cartoon effect to an image.
class cartoonizer:
      
      
upload()
cartoon_img= Cartoonizer() 
res = cartoon_img.cartoonify(Image) 
  
cv2.imwrite("Comic", res) 

# show cartoonified image 
cv2.imshow("CartoonVersion", res)  

# destroy all windows
cv2.waitKey(0) 
cv2.destroyAllWindows() 

# Cartooning an Image using OpenCV – Python
Implementation of Digital Image Smoothing Filters, Edge Detection Algorithms in order to create a cartoon effect.

## Cartonify.py
This file import all required required modules.
  1.easygui: Imported to open a file box. It will allow us to select any file from our system.
  2.Matplotlib: For visualization and plotting of images.
  
## Cartoonizer.py
This file contains a Cartoonizer class that applies a cartoon effect to an Image.
  ## Detecting and emphasizing edges
    a)Convert the original color image into grayscale
    b)Using adaptive thresholding to detect and emphasize the edges in an edge mask-
       For detecting edges here we use adaptive thresholdig that will give us more satisfying results in compared to simple thresholding. 
       We use cv2.adaptiveThreshold() function which calculates the threshold for smaller regions of the image. 
       In this way, we get different thresholds for different regions of the same image. That is the reason why this function is very suitable for our goal.
       It will emphasize black edges around objects in the image.
    c)For better illustration, we apply a median blur to reduce image noise
    
  ## Image Filtering
     a)Implementation of bilateral filter for edge preserving and noise reduction-
      Similarly to the Gaussian, bilateral filter replaces each pixel value with a weighted average of nearby pixel values. 
      However, the difference between these two filters is that a bilateral filter takes into account the variation of pixel intensities in order to preserve edges. 
      The idea is that two nearby pixels that occupy nearby spatial locations also must have some similarity in the intensity levels.
  
 ## Creating a Cartoon effect
   Masking edged image with our colored image by using bitwise_and operation.
 

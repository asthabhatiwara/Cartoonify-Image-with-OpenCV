
# Cartooning an Image using OpenCV – Python
Implementation of Digital Image Smoothing Filters, Edge Detection Algorithms in order to create a cartoon effect.

## Cartoonify.py
This file imports all required required modules.<br/>
   1. easygui: Imported to open a file box. It will allow us to select any file from our system.<br/>
   2. Matplotlib: For visualization and plotting of images.


## Cartoonizer.py
This file contains a Cartoonizer class that applies a cartoon effect to an Image.

### Detecting and Emphasizing Edges
   1. This class converts the original color image into grayscale
   2. Implmented adaptive thresholding to detect and emphasize the edges in an edge mask-
        + For detecting edges here we use adaptive thresholdig that will give us more satisfying results in compared to simple thresholding. 
        + We use cv2.adaptiveThreshold() function which calculates the threshold for smaller regions of the image.  It will emphasize black edges around objects in the image. 
   3. For better illustration, we apply a median blur to reduce image noise

### Image Filtering
   1. Implemented bilateral filter for edge preserving and noise reduction-
        + Similarly to the Gaussian, bilateral filter replaces each pixel value with a weighted average of nearby pixel values.
        + A bilateral filter takes into account the variation of pixel intensities in order to preserve edges.

 ### Creating a Cartoon effect
   Masking edged image with our colored image by using bitwise_and operation.

#A cartoonizer class that applies a cartoon effect to an image. 
#We use bilateral filter and adaptive thresholding to create a cartoon effect. 

class cartoonizer:

    def nothing(self):
       pass

    def cartoonify(self,Image):

      # reading images
      original_img= cv2.imread(Image)
      original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)  #convert bgr to rgb
    

    # if image or path doesn't exists
    if originalmage is None:
        print("Couldn't find any image. Choose an another appropriate file")
        sys.exit()

    #Resize the image 
    ReSized1 = cv2.resize(originalmage, (1200, 740))
    plt.imshow(ReSized1, cmap='gray')


    #converting an image to grayscale 
    grayScaleImage= cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (1200, 740))
    plt.imshow(ReSized2, cmap='gray')


 ## edge detection and enhancment 

    #applying median blur for smoothing an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (1200, 740))
    plt.imshow(ReSized3, cmap='gray')


    #retrieving the edges for cartoon effect by using adaptive thresholding algorithm of type binary and ADAPTIVE_THRESH_MEAN_C for threshold method
    mask_Edges = cv2.adaptiveThreshold(smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)  # mask for cartoon effect
    ReSized4 = cv2.resize(getEdge, (1200, 740))
    plt.imshow(ReSized4, cmap='gray')


 ##  cartoon effect 


    #applying bilateral filter to remove noise 
    colorImage = cv2.bilateralFilter(originalmage, 9, 250, 250)  
    ReSized5 = cv2.resize(colorImage, (1200, 740))
    plt.imshow(ReSized5, cmap='gray')


    # applly the mask for cartooning effect using bitwise_and operation 
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=mask_Edges)
    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    plt.imshow(ReSized6, cmap='gray')

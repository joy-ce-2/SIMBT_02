# Importing open-cv library                                       
import cv2 

# Image loading 
image = cv2.imread('la.jpg')                      

# Displaying original image
cv2.imshow('Original Image',image)

# Grayscale Conversion
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 

# Invert colors
inverted = cv2.bitwise_not(gray)

# Gaussian blur
blur = cv2.GaussianBlur(inverted,(1,1),0)

# Edge Detection using Canny Edge Detector
edge = cv2.Canny(blur,80,150)

# Thresholding
ret , thresh = cv2.threshold(edge,2,125,type=cv2.THRESH_BINARY)

# Dilation
dilated = cv2.dilate(thresh,(9,9),iterations=2)

# Combining
combine = cv2.bitwise_and(inverted,dilated)

# Final Sketch
sketch = cv2.bitwise_not(combine)

# Displaying final sketch
cv2.imshow('Final Sketch',sketch)

#Saving Final sketch
cv2.imwrite('Final sketch.jpg',sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
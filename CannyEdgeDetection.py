import numpy as np
import matplotlib.pyplot as plt	import cv2	
# Load image and convert it from BGR to RGB
image = cv2.cvtColor(cv2.imread("folder/imageName.jpg"), cv2.COLOR_BGR2RGB)

def resize(img, height=800):
""" Resize image to given height """
rat = height / img.shape[0]
return cv2.resize(img, (int(rat * img.shape[1]), height))
# Resize and convert to grayscale
img = cv2.cvtColor(resize(image), cv2.COLOR_BGR2GRAY)	
# Bilateral filter preserv edges
img = cv2.bilateralFilter(img, 9, 75, 75)	
# Create black and white image based on adaptive threshold
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 4)	
# Median filter clears small details
img = cv2.medianBlur(img, 11)	
# Add black border in case that page is touching an image border
img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0, 0, 0])	
edges = cv2.Canny(img, 200, 250)

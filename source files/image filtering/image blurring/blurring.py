import cv2
import numpy as np

#take image as input
inp_image = cv2.imread("input.jpeg")

#blurring image by gaussian blurring
blurred_image = cv2.GaussianBlur(inp_image,(5,5),0)

#showing after blurring image
cv2.imshow("Showing Image (press any key to exit)", blurred_image)
cv2.waitKey(0)                              #display image till pressing Any Key

#save blurred image
cv2.imwrite('blurred_output.jpeg', blurred_image)
import cv2
import numpy as np

#take image as input
inp_image = cv2.imread("input.jpeg")

#sharpen image by averaging the kernel with 2D Convolution
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen_image = cv2.filter2D(inp_image, -1, kernel)

#showing after sharping image
cv2.imshow("Showing Image (press any key to exit)", sharpen_image)
cv2.waitKey(0)

#save shrped image
cv2.imwrite('sharpen_output.jpeg', sharpen_image)
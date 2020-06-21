import cv2

#take image as input
inp_image = cv2.imread("input.jpeg")

#invert image
inverted_image = cv2.bitwise_not(inp_image)

#showing after inverting
cv2.imshow("Showing Image (press any key to exit)", inverted_image)
cv2.waitKey(0)

#save inverted image
cv2.imwrite('inverted_output.jpeg', inverted_image)
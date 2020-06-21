import cv2

#take image as input
inp_image = cv2.imread("input.jpeg")

#see current image size
height, width, channels = inp_image.shape
print(height, width, channels)

#showing image
cv2.imshow("Showing Image (press any key to exit)", inp_image)
cv2.waitKey(0)                      #display image till pressing Any Key

#resize image
resized_image = cv2.resize(inp_image, (300, 300))

#showing after resizing
cv2.imshow("Showing Image (press any key to exit)", resized_image)
cv2.waitKey(0)

#save resized image
cv2.imwrite('resized_output.jpeg', resized_image)



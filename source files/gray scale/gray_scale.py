import cv2

#take image as input
inp_image = cv2.imread("input.jpeg")

#convert image to gray scale
gray_image = cv2.cvtColor(inp_image, cv2.COLOR_BGR2GRAY)

#showing after making gray 
cv2.imshow("Showing Image (press any key to exit)", gray_image)
cv2.waitKey(0)                              #display image till pressing Any Key

#save gray image
cv2.imwrite('gray_output.jpeg', gray_image)


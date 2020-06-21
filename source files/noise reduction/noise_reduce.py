import cv2

#take image as input
inp_image = cv2.imread("input.jpeg")

#removing noise by Bilateral Filtering
noise_reduced_image = cv2.bilateralFilter(inp_image,9,75,75)

#showing after noise reducing
cv2.imshow("Showing Image (press any key to exit)", noise_reduced_image)
cv2.waitKey(0)                              #display image till pressing Any Key

#save noise reduced image
cv2.imwrite('noise_reduced_output.jpeg', noise_reduced_image)
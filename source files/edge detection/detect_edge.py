import cv2

input_image = cv2.imread('input.jpeg',0)

image_edges = cv2.Canny(input_image,100,200)

#showing the edges of the image
cv2.imshow("Showing Image (press any key to exit)", image_edges)
cv2.waitKey(0)

#save image edges
cv2.imwrite('edges_output.jpeg', image_edges)

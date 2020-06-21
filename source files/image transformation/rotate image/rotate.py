import cv2
import skimage

#take image as input
inp_image = skimage.io.imread("input.jpeg")

rotated_image = skimage.transform.rotate(inp_image, 90)

#showing after rotation 
cv2.imshow("Showing Image (press any key to exit)", rotated_image)
cv2.waitKey(0)  

#save rotated image
skimage.io.imsave('rotated_output.jpeg', rotated_image)


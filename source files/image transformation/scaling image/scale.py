import cv2
import skimage

#take image as input
inp_image = skimage.io.imread("input.jpeg")

#scaling image
scaled_image = skimage.transform.rescale(inp_image, .5)     #scaling by 50%

#showing image after scaling
cv2.imshow("Showing Image (press any key to exit)", scaled_image)
cv2.waitKey(0)  

#save scaled image
skimage.io.imsave('scaled_output.jpeg', scaled_image)


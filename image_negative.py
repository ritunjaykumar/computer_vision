import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def makeNegativeImage(img):
	(w,h,c)=img.shape # w means width h means heigh and c means color channels
	for i in range(w):
		for j in range(h):
			color_list=img[i][j]
			color_list[0]=255-color_list[0] # for red channel
			color_list[1]=255-color_list[1] # for green channel
			color_list[2]=255-color_list[2] # for blue channel
			# make negative images
			img[i][j]=color_list
			img1=img
	return img1
  
def displayImage(img):
	plt.subplot(111),plt.imshow(img),plt.title("negative image")
	plt.show()
  
def main():
	img=cv.imread("/root/Documents/ip/images/sneakers.jpg")
  img = img[...,::-1]
  img1=makeNegativeImage(img)
  diplayImage(img)
  
if __name__ == '__main__':
	main()

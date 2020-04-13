import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def image_flip(img):
	(w,h,c)=img.shape
	print((w,h,c))
	temp_img=np.ones((w,h,3), np.uint8)
	for i in range(w):
		for j in range(h//2,h):
			temp_img[i][h-j]=img[i][j]
			temp_img[i][j]=img[i][j]
	return temp_img

def show_img(img):
	plt.subplot(111),plt.imshow(img),plt.title("mirror image")
	plt.show()
def main():
	img=cv.imread("/root/Documents/ip/images/rooster.jpg")
	img = img[...,::-1] #convert bgr to rgb
	img=image_flip(img)
	show_img(img)
  
if __name__ == '__main__':
	main()

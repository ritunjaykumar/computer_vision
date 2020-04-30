import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def grayImage(img):
    h, w = img.shape[:2]
    one_mat = np.ones((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            color_list = img[i, j]
            sum_inst = int(color_list[0]) + int(color_list[1]) + int(color_list[2])
            one_mat[i, j] = np.uint8(sum_inst // 3)
    return one_mat


img = cv.imread("/root/Documents/ip/resources/images/satellite.png")
# img = img[..., ::-1]
threshold = 100
gray_img = grayImage(img)
h, w = gray_img.shape[:2]
print(gray_img.shape)
for i in range(h):
    for j in range(w):
        a = gray_img[i, j]
        b = 255 if a > threshold else 0
        gray_img[i, j] = b
# plt.subplot(111), plt.imshow(gray_img), plt.title("binary image")
# plt.show()
cv.imshow("original", img)
cv.imshow("image", gray_img)
cv.waitKey(0)

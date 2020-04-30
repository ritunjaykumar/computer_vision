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


def main():
    img = cv.imread("/root/Documents/ip/resources/images/file.png")
    img = img[..., ::-1]
    gray_image = grayImage(img)
    cv.imshow("gray image", gray_image)
    cv.waitKey(0)
    return


if __name__ == '__main__':
    main()

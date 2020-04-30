import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def average( mat ):
    mat_size = mat.shape[0]
    mod_value = mat_size**2
    # print()
    # print(mat)
    r_sum = 0
    b_sum = 0
    g_sum = 0
    for i in range(mat_size):
        for j in range(mat_size):
            intensity = mat[i, j]
            r_sum += int(intensity[0])
            b_sum += int(intensity[1])
            g_sum += int(intensity[2])
        r_avg =(r_sum // mod_value)
        b_avg =(b_sum // mod_value)
        g_avg = (g_sum // mod_value)
    # print("sum : {} {} {} ".format(r_sum, b_sum, g_sum))
    # print("avg : {} {} {} ".format(r_avg, b_avg, g_avg))
    return np.uint8([r_avg, b_avg, g_avg])


def gaussianBlur(img, alpha=3):
    h, w = img.shape[:2]
    # dup_img=np.asarray(img)
    dup_img = np.ones((h, w, 3), dtype=np.uint8)
    for i in range(0, h - (alpha - 1)):
        for j in range(0, w - (alpha - 1)):
            # average(img[i:i + alpha, j:j + alpha])
            dup_img[i, j] = average(img[i:i + alpha, j:j + alpha])
    return dup_img


img = cv.imread("/root/Documents/ip/resources/images/file.png")
img = img[..., ::-1]  # convert into bgr to rgb using numpy
dup_img = gaussianBlur(img, alpha=5)
plt.subplot(121), plt.imshow(img), plt.title("original images")
plt.subplot(122), plt.imshow(dup_img), plt.title("duplicate images")
plt.show()

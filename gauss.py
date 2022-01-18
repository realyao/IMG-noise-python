import cv2
import math
import numpy as np
import os
import random
file = 'datatest\\' #源数据文件夹
 
for file_img in os.listdir(file): 
    img = cv2.imread(file + file_img) 
    gauss_nois = np.zeros(img.shape, dtype=np.uint8)
    m = (0,0,0)
    s = (100, 100, 100)
    cv2.randn(gauss_nois, m, s)
    noised_img = img + gauss_nois
    cv2.imwrite('result_gauss\\' + file_img, noised_img) # 保存的文件夹
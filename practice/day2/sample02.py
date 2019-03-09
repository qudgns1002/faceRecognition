#coding: utf-8
#sample02.py

import cv2
import numpy as np

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    cv2.imshow('sample01.png/color', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('sample01.png/gray', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
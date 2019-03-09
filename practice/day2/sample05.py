#coding: utf-8
#sample05.py

import cv2
import numpy as np

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    cv2.imshow('sample01.png', img)

    inv = cv2.bitwise_not(img) #ビット反転

    cv2.imshow('sample01.png/inv', inv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except FileNotFoundError as e:
    print(e)
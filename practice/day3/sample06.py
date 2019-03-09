#coding: utf-8
#sample06.py

import cv2

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    cv2.imshow('sample01', img) #オリジナル

    dst1 = cv2.flip(img, 0) #上下反転
    cv2.imshow('sample02', dst1)

    dst2 = cv2.flip(img, 1) #右左反転
    cv2.imshow('sample03', dst2)

    dst3 = cv2.flip(img, -1) #上下右左反転
    cv2.imshow('sample04', dst3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
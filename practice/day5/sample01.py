#coding : utf-8
#sample01.py

import cv2

try:
    img = cv2.imread('c:\sample\sample06.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    cv2.imshow('sample01', img)

    ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('sample02', th)

    #近傍の平均からCを引いた値をしきい値とする
    ada1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('sample03', ada1)

    #近傍の重み付け平均値からCを引いた値をしきい値とする
    ada2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('sample04', ada2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
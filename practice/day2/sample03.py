#coding: utf-8
#sample03.py

import cv2

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    blue, green, red = cv2.split(img)
    cv2.imshow('sample01.png/blue', blue)
    cv2.imshow('sample01.png/green', green)
    cv2.imshow('sample01.png/red', red)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)

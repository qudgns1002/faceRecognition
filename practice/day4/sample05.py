#coding: utf-8
#sample05.py

import cv2
import numpy as np

try:
    img1 = cv2.imread('c:\sample\sample05.png', cv2.IMREAD_COLOR)
    if img1 is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    img2 = cv2.imread('c:\sample\sample06.png', cv2.IMREAD_COLOR)
    if img2 is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    img_mask = np.zeros((680, 1024), np.uint8)

    #マスクの作成
    img_mask = cv2.circle(img_mask, (236, 340), 100, (255, 255, 255), -1)
    triangle = np.array([[512, 240], [412, 440], [612, 440]])
    img_mask = cv2.fillConvexPoly(img_mask, triangle, (255, 255, 255))
    rectangle = np.array([[688, 240], [688, 440], [888, 440], [888, 240]])
    img_mask = cv2.fillConvexPoly(img_mask, rectangle, (255, 255, 255))

    #マスクを使って加算
    add1 = cv2.add(img1, img2, mask=img_mask)
    cv2.imshow('sample01', add1)

    cv2.waitKey(0)
    cv2.detroyAllWindows()

except FileNotFoundError as e:
    print(e)
#coding: utf-8
#sample02.py

import cv2

try:
    img1 = cv2.imread('c:\sample\sample05.png', cv2.IMREAD_COLOR)
    if img1 is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    img2 = cv2.imread('c:\sample\sample06.png', cv2.IMREAD_COLOR)
    if img2 is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    #absdiff関数
    #abs56 = cv2.absdiff(img1, img2)
    #cv2.imshow('abs56', abs56)

    #sample05.png - sample06.png
    #dst56 = img1 - img2
    #cv2.imshow('5-6', dst56)

    #sample06.png - sample05.png
    #dst65 = img2 - img1
    #cv2.imshow('6-5', dst65)

    #画像の乗算
    multi56 = cv2.multiply(img1, img2)
    cv2.imshow('multi56', multi56)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
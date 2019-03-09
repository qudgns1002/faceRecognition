#coding: utf-8
#sample01.py

import cv2

try:
    img1 = cv2.imread('c:\sample\sample05.png', cv2.IMREAD_COLOR)
    if img1 is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    img2 = cv2.imread('c:\sample\sample06.png', cv2.IMREAD_COLOR)
    if img2 is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    #2つの画像の加算
    #add56 = cv2.add(img1, img2)
    #cv2.imshow('sample56', add56)

    #+演算子に変更する
    dst56 = img1 + img2
    cv2.imshow('sample56', dst56)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
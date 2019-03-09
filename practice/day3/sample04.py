#coding: utf-8
#sample04.py

import cv2

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    #目の部分の座標
    img = img[234: 325, 312: 366]
    cv2.imshow('sample01', img)

    #8倍にする
    size = (img.shape[1] * 8, img.shape[0] * 8)

    #最近傍補間
    dst1 = cv2.resize(img, size, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('sample02', dst1)

    #ピクセル領域の関係
    dst2 = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    cv2.imshow('sample03', dst2)

    #バイキュービック
    dst3 = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('sample04', dst3)

    #ランシォシュ
    dst4 = cv2.resize(img, size, interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow('sample05', dst4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
    
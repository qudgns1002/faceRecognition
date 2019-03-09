#coding: utf-8
#sample01.py

import cv2

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    x = 118
    y = 55
    #切り抜きたい画像のサイズ 567, 637
    width = 570 - x
    height = 640 - y

    #Pythonのスライス機能で読み込んだndarrayから切り出す
    dst = img[y: (y+height), x: (x+width)]

    cv2.imshow('sample01', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)


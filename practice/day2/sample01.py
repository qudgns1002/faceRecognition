#coding: utf-8
#sample01.py

import cv2

try:
    #グレースケールで読み込む
    img1 = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_GRAYSCALE)
    if img1 is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    #カラー画像で読み込む
    img2 = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img2 is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    print(f'img1 : {img1.shape}') #縦
    print(f'img2 : {img2.shape}') #横

except FileNotFoundError as e:
    print(e)
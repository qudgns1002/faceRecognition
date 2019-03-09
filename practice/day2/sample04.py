#coding: utf-8
#sample04.py

import cv2
import numpy as np

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')

    height, width = img.shape[:2]
    #読み込んだ画像と同じサイズ/同じデータタイプでシングルチャンネルのゼロデータを作成
    zeros = np.zeros((height, width), img.dtype)

    #読み込んだ画像の各色を分離
    blue, green, red = cv2.split(img)

    #分離した色成分と、ゼロデータを合成して3チャンネルカラー画像を生成
    blue = cv2.merge((blue, zeros, zeros))
    green = cv2.merge((zeros, green, zeros))
    red = cv2.merge((zeros, zeros, red))

    cv2.imshow('sample_blue', blue)
    cv2.imshow('sample_green', green)
    cv2.imshow('sample_red', red)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except FileNotFoundError as e:
    print(e)
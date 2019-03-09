#coding: utf-8
#sample06.py

import cv2

try:
    
    img = cv2.imread('C:\\sample\\target\\005.png', cv2.COLOR_BGR2GRAY)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    #顔認識用のXMLファイル
    #環境に応じてパスを書き換える
    filename = 'C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
    #filename = 'C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_eye.xml'
    
    cascade = cv2.CascadeClassifier(filename)
    if cascade is None:
        raise FileNotFoundError('ファイルが見つかりません。')
    
    #顔の検出
    face = cascade.detectMultiScale(img)

    if len(face) > 0:
        for r in face:
            print(r)
            x, y = r[0:2]
            width, height = r[0:2] + r[2:4]
            #検出した部分に四角形を描く
            cv2.rectangle(img, (x, y), (width, height), (255, 255, 255), thickness=2)
    else:
        print('顔が見つかりません')

    #画像データが大きいと表示しきれないのでファイルに保存する
    cv2.imwrite('c:\sample\dobj.jpg', img)
    cv2.imshow('sample01', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
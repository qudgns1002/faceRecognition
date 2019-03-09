import cv2

try:
    img = cv2.imread('c:\sample\sample01.png', cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('file can not be found')

    cv2.imshow('sample01', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')     # 직사각형을 그릴 영상

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img, (830,30), (1000,200), (0,0,255), 2)     # 직사각형 그리기 (이미지, 직사각형 좌상 좌표, 직사각형 우하 좌표, 색상, 선 두께)

cv.putText(img, 'laugh', (830,24), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)     # 글씨 쓰기 (이미지, 쓸 문자열, 문자열 좌하 좌표, 폰트 종류, 글자 크기, 색상, 글자 두께)

cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()
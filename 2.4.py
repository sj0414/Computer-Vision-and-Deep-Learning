import cv2 as cv
import sys

#img=cv.imread('soccer.jpg')
img=cv.imread('/Users/koosuhjung/Desktop/computerVision/source_4548_1/source/ch2/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyAllWindows()

import cv2 as cv     # cv2를 cv로 불러오기
import sys           # sys 모듈 불러오기

img=cv.imread('soccer.jpg')     # soccer.jpg 읽어오기

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')     # 파일이 없으면 출력

cv.imshow('Image Display', img)        # (윈도우 이름, 이미지)

cv.waitKey()     # 키 눌릴 때까지 기다림
cv.destroyAllWindows()     # 키 눌리면 윈도우 닫기

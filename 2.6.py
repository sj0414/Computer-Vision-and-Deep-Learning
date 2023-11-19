import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)     # 카메라와 연결 시도 (웹 캠 번호(하나면 0), 비디오 화면에 바로 나타나게)

if not cap.isOpened():     # 웹 캠 연결 실패 시 (isOpened = false)
    sys.exit('카메라 연결 실패')     # 오류 메시지 출력 후 프로그램 종료

frames = []

while True:
    ret, frame = cap.read()     # 비디오를 구성하는 프레임 획득 (ret에 성공 여부 저장, frame에 프레임 저장)

    if not ret:     # 프레임 획득 실패 시 루프 빠져나감
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    cv.imshow('Video display', frame)     # 획득 영상 디스플레이

    key = cv.waitKey(1)     # 1밀리초 동안 키보드 입력 기다림
    if key == ord('c'):     # 'c' 키가 들어오면 프레임을 리스트에 추가
        frames.append(frame)
    elif key == ord('q'):   # 'q' 키가 들어오면 루프를 빠져나감
        break
    #if key == ord('q'):     # 'q' 키가 들어오면 루프를 빠져나감
    #    break

cap.release()     # 카메라와 연결을 끊음
#cap.destroyAllWindows()
cv.destroyAllWindows()

if len(frames) > 0:     # 수집된 영상이 있으면
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):     # 최대 3개까지 이어 붙임 (영상이 너무 커서 밖으로 나가는 것 방지)
        imgs = np.hstack((imgs, frames[i]))

    cv.imshow('collected images', imgs)

    cv.waitKey()
    cv.destroyAllWindows()
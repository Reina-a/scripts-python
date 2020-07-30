from cv2 import cv2

cap = cv2.VideoCapture('k3.mp4')

if cap.isOpened():
    print('Open successfully!')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(frame_count)
    print('fps: ', fps,'width: ',width,'height: ',height)

    for i in range(int(frame_count)):
        ret, frame = cap.read()
        filename = 'out/' + 'frame' + "{:0>4d}".format(i) + '.jpg'
        cv2.imwrite(filename, frame)
else:
    print('Error occurred when opening the video.')

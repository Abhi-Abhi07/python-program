import cv2
cap=cv2.VideoCapture("D:\\video1.mp4")
total=cap.get(7)
print(total)

# 14sec*30frame=420
cap.set(1,420)
ret,frame=cap.read()
cv2.imwrite("r"+".jpg",frame)
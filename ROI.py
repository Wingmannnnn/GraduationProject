import cv2

# 設定視窗名稱
window_name = 'Webcam'

# 開啟 webcam
cap = cv2.VideoCapture(0)

# 設定視窗大小
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)

# 顯示影像
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow(window_name, frame)

    # 按下 'q' 鍵結束程式
    if cv2.waitKey(1) == 27:
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()

import cv2

# 讀取游泳影片
cap = cv2.VideoCapture("swimming_sample.mp4")

while cap.isOpened():
  success, frame = cap.read()
  if not success:
    print("影片讀取結束或找不到檔案。")
    break

  # 顯示影片畫面
  cv2.imshow("Swimming Video Test", frame)

  # 按下 q 鍵可以關閉視窗
  if cv2.waitKey(25) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()

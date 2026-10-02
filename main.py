import cv2

# 開啟游泳影片（請確保你的影片檔名正確，或是改成你的影片路徑）
cap = cv2.VideoCapture("swimming_sample.mp4")

while cap.isOpened():
  success, frame = cap.read()
  if not success:
    print("影片讀取結束或找不到檔案。")
    break

  # 取得影片的寬度與高度
  height, width, _ = frame.shape

  # ==========================================
  # 定義輔助線的位置（你可以根據影片畫面自行調整數值比例）
  # ==========================================

  # 1. 畫一條「水平基準線」（例如代表水面或身體平穩基準線）
  # 參數格式：cv2.line(畫布, 起點(x, y), 終點(x, y), 顏色(B, G, R), 線條粗細)
  line_y = int(height * 0.4)  # 位於畫面高度的 40% 處
  cv2.line(
      frame,
      (0, line_y),
      (width, line_y),
      (0, 255, 255),
      2,
  )  # 黃色線 (B=0, G=255, R=255)

  # 2. 畫一個「泳道或觀察區域框」（框住學員主要活動的範圍）
  box_x1 = int(width * 0.2)
  box_y1 = int(height * 0.1)
  box_x2 = int(width * 0.8)
  box_y2 = int(height * 0.9)
  cv2.rectangle(
      frame, (box_x1, box_y1), (box_x2, box_y2), (255, 0, 0), 2
  )  # 藍色框 (B=255, G=0, R=0)

  # 3. 在畫面上加上文字說明
  cv2.putText(
      frame,
      "Reference Line: Water Level / Body Balance",
      (30, 40),
      cv2.FONT_HERSHEY_SIMPLEX,
      0.7,
      (0, 255, 255),
      2,
  )

  cv2.putText(
      frame,
      "Swim Lane Zone",
      (box_x1 + 10, box_y1 + 30),
      cv2.FONT_HERSHEY_SIMPLEX,
      0.6,
      (255, 0, 0),
      2,
  )

  # ==========================================
  # 顯示處理後的畫面
  # ==========================================
  cv2.imshow("Swimming Pool Analysis - Reference Lines", frame)

  # 按下 'q' 鍵可以關閉視窗
  if cv2.waitKey(25) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()

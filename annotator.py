import csv
from datetime import datetime
import cv2

# 開啟游泳教學影片
video_path = "swimming_sample.mp4"
cap = cv2.VideoCapture(video_path)

# 建立 CSV 紀錄檔來儲存自傷行為發生的時間點
csv_file = open("behavior_log.csv", mode="w", newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["Frame_Number", "Timestamp_Sec", "Event"])

fps = cap.get(cv2.CAP_PROP_FPS)
print("操作說明：")
print("  - 播放時按下 's' 鍵，可在 CSV 紀錄當下影格發生「自傷/敲頭行為」")
print("  - 按下 'q' 鍵退出")

while cap.isOpened():
  ret, frame = cap.read()
  if not ret:
    break

  current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
  current_sec = current_frame / fps if fps > 0 else 0

  # 在畫面上顯示當前秒數與操作提示
  cv2.putText(
      frame,
      f"Time: {current_sec:.2f}s",
      (30, 40),
      cv2.FONT_HERSHEY_SIMPLEX,
      0.8,
      (0, 255, 0),
      2,
  )
  cv2.putText(
      frame,
      "Press 's' to log self-injury event",
      (30, 80),
      cv2.FONT_HERSHEY_SIMPLEX,
      0.6,
      (0, 0, 255),
      2,
  )

  cv2.imshow("Swimming Behavior Annotation Tool", frame)

  key = cv2.waitKey(30) & 0xFF
  if key == ord("s"):
    # 記錄當下事件
    writer.writerow([current_frame, round(current_sec, 2), "Head_Hitting"])
    print(f"已記錄自傷事件於: {current_sec:.2f} 秒")
  elif key == ord("q"):
    break

cap.release()
csv_file.close()
cv2.destroyAllWindows()

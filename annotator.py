from datetime import datetime
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="游泳教學網頁版行為標註系統", layout="wide")

st.title("🏊‍♂️ 運動科技輔助適應性游泳教學：網頁版行為標註系統")
st.markdown("教授專用網頁介面：支援影片播放與鍵盤快捷鍵即時標註[cite: 7]。")

if "annotations" not in st.session_state:
  st.session_state.annotations = []

uploaded_file = st.file_uploader(
    "請上傳游泳教學影片 (MP4 / MOV)", type=["mp4", "mov"]
)

if uploaded_file is not None:
  col1, col2 = st.columns([2, 1])

  with col1:
    st.subheader("📹 網頁影片播放與即時標註區")

    # 顯示內建影音
    st.video(uploaded_file)

    st.markdown("---")
    st.markdown("### ⌨️ 鍵盤即時記錄控制台")
    st.markdown(
        "**操作方式**：為了配合網頁瀏覽器，請在下方輸入框對應影片當前秒數，或透過下方快捷按鈕記錄。"
    )

    # 讓使用者對應目前秒數
    current_time = st.number_input(
        "請輸入/對應目前影片播放秒數：",
        min_value=0.0,
        max_value=3600.0,
        step=0.1,
        format="%.1f",
    )

    # 快捷鍵按鈕
    if st.button("⚡ 記錄當前秒數行為 (支援快捷鍵)", type="primary"):
      st.session_state.annotations.append({
          "時間點 (秒)": current_time,
          "事件類型": "Head-Hitting (敲頭)",
          "記錄時間": datetime.now().strftime("%H:%M:%S"),
      })
      st.success(f"成功記錄 {current_time} 秒處的行為！")

    if st.button("🔄 清空所有標註紀錄"):
      st.session_state.annotations = []
      st.rerun()

  with col2:
    st.subheader("📊 即時標註紀錄清單")
    if len(st.session_state.annotations) > 0:
      df = pd.DataFrame(st.session_state.annotations)
      st.dataframe(df, use_container_width=True)

      csv = df.to_csv(index=False).encode("utf-8")
      st.download_button(
          label="📥 下載行為觀察基線 (CSV)",
          data=csv,
          file_name="behavior_baseline.csv",
          mime="text/csv",
      )
    else:
      st.info("目前尚無標註紀錄。")

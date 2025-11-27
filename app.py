import streamlit as st
from transformers import pipeline

# 1. 頁面設定
st.set_page_config(
    page_title="AI 文本檢測器",
    page_icon="🕵️‍♀️",
    layout="centered"
)

# 2. 載入模型 (使用 @st.cache_resource 避免每次重整都重新下載模型)
@st.cache_resource
def load_model():
    """
    載入 Hugging Face 的文本分類模型。
    這裡使用的是 Hello-SimpleAI/chatgpt-detector-roberta
    """
    model_name = "Hello-SimpleAI/chatgpt-detector-roberta"
    # 初始化 pipeline
    classifier = pipeline("text-classification", model=model_name)
    return classifier

# 3. 標題與說明
st.title("🕵️‍♀️ AI 文本生成檢測器")
st.markdown("""
此工具使用 **RoBERTa** 模型來分析文本，判斷其是否極有可能由 AI (如 ChatGPT) 生成。
> **注意**：AI 檢測並非 100% 準確，結果僅供參考。
""")

st.divider()

# 4. 初始化模型 (顯示載入動畫)
try:
    with st.spinner('正在載入 AI 偵測模型，初次執行可能需要幾分鐘...'):
        classifier = load_model()
except Exception as e:
    st.error(f"模型載入失敗: {e}")
    st.stop()

# 5. 使用者輸入區
user_input = st.text_area(
    "請在下方貼上要檢測的英文或中文文章 (建議長度 > 50 字):",
    height=200,
    placeholder="在此貼上文本..."
)

# 6. 分析按鈕與邏輯
if st.button("開始檢測 🔍", type="primary"):
    if not user_input.strip():
        st.warning("⚠️ 請輸入內容後再進行檢測！")
    elif len(user_input) < 30:
        st.warning("⚠️ 文本過短，可能會影響判斷準確度，請輸入更多內容。")
    else:
        with st.spinner('正在分析文本特徵...'):
            # 由於模型限制，長文本可能需要截斷，這裡簡單取前 512 個 tokens
            # 實際應用中建議切分段落檢測
            result = classifier(user_input, truncation=True, max_length=512)[0]
            
            # 解析結果
            label = result['label'] # 通常是 'ChatGPT' 或 'Human'
            score = result['score'] # 信心分數 (0.0 - 1.0)
            
            # 顯示結果 UI
            st.divider()
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("檢測結果")
                if label == 'ChatGPT' or label == 'AI':
                    st.error("🤖 高度疑似 AI 生成")
                else:
                    st.success("👤 高度疑似人類撰寫")
            
            with col2:
                st.subheader("信心指數")
                st.metric(label="AI 判定機率", value=f"{score*100:.2f}%")
                st.progress(score)

# 7. 側邊欄資訊
with st.sidebar:
    st.header("關於本工具")
    st.info("此網站使用 Streamlit 架構，並串接 Hugging Face 的 Transformers 函式庫。")
    st.markdown("---")
    st.markdown("**技術棧:**")
    st.markdown("- Python 3.9+")
    st.markdown("- Streamlit")
    st.markdown("- PyTorch")
# 🕵️‍♀️ AI 文本生成檢測器 (AI Text Detector)

這是一個基於 **Streamlit** 和 **Hugging Face Transformers** 構建的簡易 Web 應用程式。它能夠分析使用者輸入的文本，並預測該文本是由人類撰寫還是由 AI 模型（如 ChatGPT）生成的。

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b)
![HuggingFace](https://img.shields.io/badge/Transformers-4.30%2B-yellow)

## ✨ 功能特色

* **即時分析**：輸入文本後點擊按鈕，幾秒鐘內即可獲得結果。
* **視覺化結果**：透過進度條與顏色區分（紅色為 AI，綠色為人類）顯示信心指數。
* **無需 API Key**：使用開源模型，完全免費，無需申請 OpenAI Key。
* **簡潔介面**：基於 Streamlit 的響應式設計，手機或電腦皆可使用。

## 🛠️ 技術棧

* **前端框架**: [Streamlit](https://streamlit.io/)
* **機器學習庫**: [Transformers (Hugging Face)](https://huggingface.co/docs/transformers/index), [PyTorch](https://pytorch.org/)
* **預訓練模型**: [`Hello-SimpleAI/chatgpt-detector-roberta`](https://huggingface.co/Hello-SimpleAI/chatgpt-detector-roberta)
    * 此模型基於 RoBERTa 架構，針對 ChatGPT 生成的文本進行了微調。

## 🚀 快速開始

### 1. 複製專案 (或是下載程式碼)

```bash
git clone [https://github.com/your-username/ai-text-detector.git](https://github.com/your-username/ai-text-detector.git)
cd ai-text-detector


---

# 🎥 YouTube Comment Sentiment Analysis Web App

This app analyzes YouTube video comments using multilingual sentiment classification with XLM-RoBERTa.

---

## 📦 Features

* Input a YouTube video URL
* Extract **all top-level comments** using **YouTube Data API v3**
* Auto-detect & translate **non-English** comments
* Perform sentiment analysis using `cardiffnlp/twitter-xlm-roberta-base-sentiment`
* View **sentiment distribution** as **pie chart** & **histogram**
* Highlight the **most liked** comment
* Download **full results as CSV**

---

## 🔧 Tech Stack

* **Backend/UI:** Streamlit
* **NLP Model:** HuggingFace Transformers (XLM-RoBERTa)
* **Visualization:** Plotly
* **Others:** `langdetect`, `googletrans`, `pandas`, `requests`

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-user/youtube-sentiment-app.git
cd youtube-sentiment-app
```

---

### 2. Create and Activate Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Get YouTube API Key

1. Go to: [Google Cloud Console](https://console.developers.google.com/)
2. Click on **"New Project"**
3. After the project is created, go to **APIs & Services > Library**
4. Search and enable: **YouTube Data API v3**
5. Go to **Credentials > Create Credentials > API Key**
6. Copy the API key shown — you'll be prompted to paste it in the app

---

### 5. Run the App

```bash
streamlit run app.py
```

---


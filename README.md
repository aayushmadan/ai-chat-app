# AI Chat App

Flask chat app running **llama-3.3-70b-versatile**

---

## Project Structure

```
ai-chat_app/
├── app.py              # Flask backend
├── gunicorn.conf.py    # Production server config
├── requirements.txt
├── templates/
│   └── index.html      # Single-file frontend
└── README.md
```

---

## 1. Get a Groq API Key

1. Sign up at https://groq.com/
2. Go to **Console → Access Tokens**
3. Create a token

---

## 2. Local Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export GROQ_API_KEY=="access_token"
python app.py          # dev server on :5000
```
# 🤖 Gemini AI ChatBot – Real-Time WebSocket Chat with FastAPI

Gemini AI ChatBot is a sleek, real-time chatbot built with **FastAPI**, **WebSockets**, and **Gemini 2.0 Flash Lite**. It supports live-streaming replies, markdown formatting, code block rendering, and a responsive modern UI — all powered by Google’s Gemini model.

---

## 🚀 Features

- 🔌 Real-time AI chat using WebSockets
- 🤖 Gemini 2.0 Flash Lite integration (Google GenAI)
- 📝 Markdown + syntax-highlighted code support
- 🌙 Dark/Light mode toggle with responsive design
- ⚡ Modern Bootstrap-based front-end UI
- 🔐 .env-based API key loading

---

## 🛠️ Tech Stack

| Tool            | Purpose                          |
|-----------------|----------------------------------|
| FastAPI         | Backend API framework            |
| WebSocket       | Real-time chat communication     |
| Google GenAI    | Gemini 2.0 Flash Lite integration|
| HTML/CSS/JS     | Frontend chatbot UI              |
| Bootstrap 5     | Responsive layout & design       |
| Marked.js       | Markdown rendering               |
| highlight.js    | Code syntax highlighting         |

---

## ⚙️ Setup Instructions

### 🔧 Requirements

- Python 3.10+
- Gemini API Key (Google AI Studio)

### 🔌 Installation & Run

```bash
# Clone the repository
git clone https://github.com/kashifkhanai/gemini-chatbot.git
cd gemini-chatbot/backend

# Create and activate virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Run FastAPI server
uvicorn main:app --reload

```

---

## 🤝 Author

Made with  by **Muhammad Kashif**  

📧 Contact: <mkashifkhanai@gmail.com>

🔗 [LinkedIn](https://www.linkedin.com/in/muhammadxkashif) • [GitHub](https://github.com/kashifkhanai)

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

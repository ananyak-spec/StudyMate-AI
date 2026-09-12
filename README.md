# 🎓 StudyMate AI

StudyMate AI is an AI-powered student utility application that helps students understand concepts, summarize notes, generate quizzes, and improve written answers.

## 🚀 Features

- 📚 Explain a Concept
- 📝 Summarize Notes
- ❓ Generate Quiz
- ✍️ Improve My Answer
- ⚠️ Empty input validation
- 🛡️ Error handling
- 🤖 Local AI using Llama 3.2

## 🛠️ Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Requests

## 🔄 How It Works

1. Student selects a study tool.
2. Student enters study content.
3. StudyMate creates a structured prompt.
4. The prompt is sent to the local Llama 3.2 model through Ollama.
5. AI generates the response.
6. The response is displayed clearly in the application.

## ▶️ How to Run

Install the required packages:

```bash
pip install streamlit requests
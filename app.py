import streamlit as st
import requests

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 StudyMate AI")
st.subheader("Your AI-powered study companion")
st.write("Study smarter with AI-powered explanations, summaries, quizzes and answer improvement.")

st.divider()

tool = st.selectbox(
    "🧠 What would you like StudyMate to do?",
    [
        "📚 Explain a Concept",
        "📝 Summarize Notes",
        "❓ Generate Quiz",
        "✍️ Improve My Answer"
    ]
)

if tool == "📚 Explain a Concept":
    placeholder = "Example: Explain photosynthesis in simple terms..."
elif tool == "📝 Summarize Notes":
    placeholder = "Paste your notes here..."
elif tool == "❓ Generate Quiz":
    placeholder = "Paste your study material here..."
else:
    placeholder = "Paste your answer here..."

content = st.text_area(
    "📖 Enter your content",
    height=220,
    placeholder=placeholder
)

if st.button("✨ Generate", use_container_width=True):

    if not content.strip():
        st.warning("⚠️ Please enter some content first.")
        st.stop()

    if tool == "📚 Explain a Concept":
        prompt = f"""You are StudyMate AI, a friendly academic tutor.

Explain the following concept to a college student.

Requirements:
- Use simple language.
- Break the explanation into clear sections.
- Give a practical example.
- Mention key points at the end.

Concept:
{content}"""

    elif tool == "📝 Summarize Notes":
        prompt = f"""You are StudyMate AI.

Summarize the following study notes for a college student.

Requirements:
- Extract the most important ideas.
- Use bullet points.
- Keep important technical terms.
- Make the summary easy to revise before an exam.

Notes:
{content}"""

    elif tool == "❓ Generate Quiz":
        prompt = f"""You are StudyMate AI.

Create a short practice quiz from the following study material.

Requirements:
- Create 5 questions.
- Mix conceptual and factual questions.
- Provide four options for multiple-choice questions.
- Clearly show the correct answer.
- Keep questions based only on the provided material.

Study material:
{content}"""

    else:
        prompt = f"""You are StudyMate AI, an academic answer improvement assistant.

Improve the student's answer below.

Requirements:
- Preserve the original meaning.
- Correct grammar and unclear wording.
- Make the answer more precise.
- Improve academic quality.
- Give the improved answer first.
- Then briefly explain what was improved.

Student answer:
{content}"""

    with st.spinner("🤖 StudyMate is thinking..."):
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()
            answer = response.json()["response"]

            st.success("✅ Done!")
            st.markdown("## 💡 StudyMate's Answer")
            st.write(answer)

        except Exception as e:
            st.error(f"❌ Error: {e}")
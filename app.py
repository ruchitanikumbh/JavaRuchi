import streamlit as st
import google.generativeai as genai

# -----------------------------
# Configure Gemini API
# -----------------------------
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="JavaRuchi",
    page_icon="☕",
    layout="centered"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("☕ JavaRuchi")
st.sidebar.markdown("### AI Java Programming Tutor")

st.sidebar.markdown("""
### Features
- 📘 Explain Concept
- 💡 Real-Life Example
- 📝 Generate Quiz
- ✅ Feedback
- ❓ Ask Anything
""")

st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ using Streamlit + Gemini")

# -----------------------------
# Main Page
# -----------------------------
st.title("☕ JavaRuchi")
st.subheader("Learn Java Programming in a Simple and Fun Way!")

st.success("Welcome! I'm JavaRuchi 😊")

st.write(
    "I can explain Java concepts, give real-life examples, create quizzes, "
    "review your answers, and answer your Java questions."
)

# -----------------------------
# Student Level
# -----------------------------
level = st.selectbox(
    "Select Your Java Knowledge Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# -----------------------------
# Topic
# -----------------------------
topic = st.text_input(
    "Enter Java Topic",
    placeholder="Example: Variables, Loops, Arrays, OOP"
)

# -----------------------------
# Activity
# -----------------------------
option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Feedback",
        "Ask Anything"
    ]
)

# -----------------------------
# Feedback Inputs
# -----------------------------
question = ""
student_answer = ""

if option == "Feedback":
    question = st.text_area("Enter the Question")
    student_answer = st.text_area("Enter Student Answer")

# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate"):

    if option != "Feedback" and topic.strip() == "":
        st.warning("Please enter a Java topic.")
        st.stop()

    if option == "Explain Concept":

        prompt = f"""
You are JavaRuchi, a friendly and patient Java programming tutor.

The student's level is {level}.

Explain {topic} in simple and easy language.

Include:
1. Step-by-step explanation
2. One real-life example
3. Simple Java code
4. Explain the code
5. Summary
6. One practice question
"""

    elif option == "Real-Life Example":

        prompt = f"""
You are JavaRuchi.

Give one simple real-life example of {topic}.

Explain using everyday situations.

Keep it short and beginner friendly.
"""

    elif option == "Generate Quiz":

        prompt = f"""
You are JavaRuchi.

Create 5 beginner-friendly multiple-choice questions on {topic}.

Each question should have four options:
A.
B.
C.
D.

After each question provide:

Correct Answer

Simple Explanation
"""

    elif option == "Feedback":

        if question.strip() == "" or student_answer.strip() == "":
            st.warning("Please enter both the question and the student's answer.")
            st.stop()

        prompt = f"""
You are JavaRuchi.

Question:
{question}

Student Answer:
{student_answer}

Give positive and encouraging feedback.

If the answer is incorrect,
politely explain the correct answer in simple words.

Suggest one tip to improve.
"""

    else:

        prompt = topic

    with st.spinner("JavaRuchi is preparing your response..."):
        response = model.generate_content(prompt)

    st.subheader("📘 Result")
    st.markdown(response.text)

st.markdown("---")
st.caption("© JavaRuchi | AI Java Programming Tutor")

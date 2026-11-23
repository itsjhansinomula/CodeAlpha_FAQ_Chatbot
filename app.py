# CodeAlpha - Task 2: FAQ Chatbot
# Author: Jhansi Nomula

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")
st.title("🤖 FAQ Chatbot")
st.write("Ask me questions about CodeAlpha Internship, Courses, Certificates & more!")

# FAQ Dataset
faqs = {
    "What is CodeAlpha?": "CodeAlpha is a platform that provides virtual internships in Artificial Intelligence, Web Development, Data Science and more for students.",
    "How to apply for CodeAlpha internship?": "You can apply on CodeAlpha website by filling the application form and selecting your domain like AI, Web Development, etc.",
    "How long is the internship?": "CodeAlpha internship is usually for 1 month. You need to complete the tasks given in that period.",
    "Will I get a certificate?": "Yes! After completing all tasks and submitting them on GitHub + LinkedIn, you will get a Certificate of Completion from CodeAlpha.",
    "What is Artificial Intelligence?": "Artificial Intelligence is technology that makes computers think and learn like humans. Examples are ChatGPT, Google Translate, Face Recognition.",
    "What is Machine Learning?": "Machine Learning is a part of AI where computers learn from data without being explicitly programmed.",
    "What is Python?": "Python is a simple and powerful programming language used for AI, Web Development, Data Science and Automation.",
    "How to submit tasks?": "You need to upload your code on GitHub and share your project on LinkedIn with #CodeAlpha hashtag and submit the links.",
    "Is CodeAlpha internship free?": "Yes, CodeAlpha internship is free for students. You just need to complete the tasks on time.",
    "What are the tasks in AI internship?": "Task 1 is Language Translation Tool, Task 2 is FAQ Chatbot, Task 3 is Object Detection. You can choose any tasks.",
    "Hi": "Hello! 👋 How can I help you? Ask me about CodeAlpha, Internship, Certificate, AI etc.",
    "Hello": "Hello! 👋 Ask me any question about CodeAlpha Internship.",
    "Thank you": "You're welcome! 😊 All the best for your internship!"
}

questions = list(faqs.keys())
vectorizer = TfidfVectorizer().fit(questions)

def get_answer(user_q):
    user_vec = vectorizer.transform([user_q])
    q_vec = vectorizer.transform(questions)
    sim = cosine_similarity(user_vec, q_vec)
    idx = sim.argmax()
    if sim[0][idx] < 0.2:
        return "Sorry, I don't know that. Try asking about CodeAlpha, Internship, Certificate, Python, AI, or Tasks."
    return faqs[questions[idx]]

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask your question here:")

if st.button("Ask 💬"):
    if user_input.strip() != "":
        ans = get_answer(user_input)
        st.session_state.chat.append((user_input, ans))

for q, a in reversed(st.session_state.chat):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
    st.markdown("---")

st.markdown("**Suggested Questions:**")
st.write("- What is CodeAlpha?")
st.write("- Will I get a certificate?")
st.write("- How to submit tasks?")
st.write("- What is Artificial Intelligence?")

st.markdown("---")
st.markdown("**Built by Jhansi Nomula | CodeAlpha AI Internship**")

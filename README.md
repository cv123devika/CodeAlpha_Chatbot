🤖 AI Chatbot

A FAQ-based AI chatbot built with Python, Streamlit, and scikit-learn.
Ask questions and get instant answers from a pre-defined FAQ database.

🌟 Features
FAQ-based chatbot 🤖
Instant responses ⚡
Handles common AI/ML questions 💡
Simple, lightweight, and easy to extend 🛠
🛠 Tech Stack
Python
Streamlit – interactive web app
scikit-learn – TF-IDF & cosine similarity
NLTK – natural language preprocessing
🚀 How to Run
Navigate to the project folder:
cd CodeAlpha_Chatbot
Install dependencies:
pip install nltk scikit-learn streamlit
Download NLTK stopwords and punkt (if not already):
import nltk
nltk.download('punkt')
nltk.download('stopwords')
Run the chatbot:
python -m streamlit run chatbot.py
Use it:
Type your question in the input box and click Get Answer 🎯
📚 FAQ Database

The chatbot uses faq_data.py for questions and answers.
You can add more FAQs by editing the faq dictionary inside faq_data.py.

Example:

faq = {
    "What is AI?": "AI stands for Artificial Intelligence...",
    "What is ML?": "Machine Learning is a subset of AI...",
    ...
}
⚠️ Notes
Similarity threshold: 0.3
If the question is too different from the FAQ, a warning is shown:
🤔 "Sorry, I don't know the answer to that question yet!"
Perfect for small AI demos and learning purposes.
📝 License

MIT License

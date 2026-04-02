🤖 FAQ Chatbot

An interactive FAQ chatbot built with Streamlit, scikit-learn, and NLTK.
This chatbot uses TF-IDF vectorization and cosine similarity to match user queries with predefined FAQ answers.

📌 Features
- Simple and interactive Streamlit UI
- Preprocessing with NLTK (tokenization + stopword removal)
- FAQ matching using TF-IDF and cosine similarity
- Threshold-based response handling (fallback when similarity is low)
- Easy to extend by adding new FAQs

🛠️ Tech Stack
- Python 
- Streamlit – for the web interface
- scikit-learn – for TF-IDF and similarity calculation
- NLTK – for text preprocessing (tokenization, stopwords)



 Download NLTK resources
import nltk
nltk.download('punkt')
nltk.download('stopwords')


📖 Example FAQs
Some of the questions included:
- What is AI?
- What is Machine Learning?
- What is Deep Learning?
- How to install Python?
- What is Streamlit?
- Can AI replace humans?
You can easily add more FAQs by editing faq_data.py.

Run the chatbot:
python -m streamlit run chatbot.py


⚡ How It Works
- User enters a question in the Streamlit UI.
- The input is preprocessed (lowercased, tokenized, stopwords removed).
- The system computes TF-IDF vectors for all FAQ questions + user query.
- Cosine similarity is used to find the closest FAQ.
- If similarity ≥ 0.3 → return the best answer.
Otherwise → show a fallback message.

📌 Future Improvements
- Add semantic search using embeddings (e.g., Sentence Transformers).
- Support multi-turn conversations.
- Integrate with external knowledge bases.
- Deploy on Streamlit Cloud or Heroku.

🧑‍💻 Author
Developed by DEVIKA C V
Feel free to contribute or suggest improvements!






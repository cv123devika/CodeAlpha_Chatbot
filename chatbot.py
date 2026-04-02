import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from faq_data import faq

# Preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    words = [w for w in tokens if w.isalnum() and w not in stopwords.words('english')]
    return " ".join(words)

# Prepare FAQ corpus
faq_questions = list(faq.keys())
faq_answers = list(faq.values())
preprocessed_questions = [preprocess(q) for q in faq_questions]

# Streamlit UI
st.title("🤖 FAQ Chatbot")
user_input = st.text_input("Ask me a question:")

if st.button("Get Answer") and user_input:
    user_preprocessed = preprocess(user_input)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(preprocessed_questions + [user_preprocessed])
    
    cosine_sim = cosine_similarity(vectors[-1], vectors[:-1])
    best_idx = cosine_sim.argmax()
    
    # Check if similarity is strong enough (0.3 threshold)
    if cosine_sim[0, best_idx] < 0.3:
        st.warning("🤔 Sorry, I don't know the answer to that question yet!")
    else:
        st.success(faq_answers[best_idx])
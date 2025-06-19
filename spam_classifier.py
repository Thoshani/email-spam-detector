import re
import joblib

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return text.strip()

def predict_spam(email_text):
    cleaned = clean_text(email_text)
    vect = vectorizer.transform([cleaned])
    pred = model.predict(vect)[0]
    return "spam" if pred == 1 else "ham"

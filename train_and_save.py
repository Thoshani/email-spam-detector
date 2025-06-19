import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ✅ Read correct columns
df = pd.read_csv("spam.csv", encoding="ISO-8859-1")[["v1", "v2"]]
df.columns = ["label", "text"]  # Rename to standard names
df["label"] = df["label"].map({"ham": 0, "spam": 1})  # Convert to 0 or 1

# ✅ Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    return text.strip()

df["text"] = df["text"].apply(clean_text)

# ✅ Vectorize
tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df["text"])
y = df["label"]

# ✅ Train and save
model = MultinomialNB()
model.fit(X, y)

joblib.dump(model, "spam_model.pkl")
joblib.dump(tfidf, "tfidf_vectorizer.pkl")

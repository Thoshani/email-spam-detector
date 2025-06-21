# email-spam-detector
#  Email Spam Detection Web App


##  Project Code Availability

The **full source code** for the Email Spam Detection project is uploaded in this repository.

You can choose from **two options**:
option 1
# 📧 Email Spam Detection using Naive Bayes

This project implements a simple yet effective email spam detection system using Natural Language Processing (NLP) and machine learning techniques. It classifies incoming messages as **"spam"** or **"ham"** (not spam) using a Multinomial Naive Bayes classifier.

---

## 🚀 Features

- 📑 Preprocessing of text: cleaning, tokenization, and stopword removal
- 🧠 Feature extraction using TF-IDF
- 🤖 Naive Bayes classification (MultinomialNB, BernoulliNB, and GaussianNB)
- 📊 Evaluation with accuracy, precision, recall, and confusion matrix
- 📈 Data visualization (pie chart of spam vs ham)
- 🧹 Duplicate removal and null check

---

## 🛠️ Tech Stack

- Python
- Jupyter Notebook
- Scikit-learn
- Pandas
- Matplotlib / Seaborn
- NLTK (for stopword removal)
- NumPy

---

## 📂 Dataset

The dataset is a labeled collection of SMS messages containing two columns:

- `v1`: Label (`spam` or `ham`)
- `v2`: The message text

Make sure the file is named something like `spam.csv` and placed correctly for loading.

---

## 🧪 Workflow

### 1. **Load & Clean Dataset**
- Read CSV using pandas
- Remove duplicates and nulls

### 2. **Text Preprocessing**
- Remove punctuation and numbers
- Convert to lowercase and remove stopwords

### 3. **Vectorization**
- Use `TfidfVectorizer` to convert text to numerical features

### 4. **Model Training**
- Use `MultinomialNB` classifier
- Compare with `BernoulliNB` and `GaussianNB`

### 5. **Evaluation**
- Accuracy
- Precision
- Recall
- Confusion matrix

---

## 📊 Sample Results

text
Model Evaluation:
Accuracy:  97.12%
Precision: 0.96
Recall:    0.94

option 2
###  1. Jupyter Notebook (`email_spam_detection.ipynb`)
- Ideal for understanding the step-by-step machine learning pipeline
- Includes data preprocessing, TF-IDF vectorization, model training, and testing

###  2. Python Scripts (`train_and_save.py`, `spam_classifier.py`, `app.py`)
- Fully converted for integration into a **Flask web app**
- Ready to be run directly without needing Jupyter

You can use either version depending on your preference:
- Use the **notebook** to study the ML process
- Use the **scripts** to run the full web application

 Both have been tested and work independently or together.
===================================================================================================================================================================
This is a simple yet powerful machine learning web app that detects whether an email is **spam** or **ham** (not spam) using a Naive Bayes classifier and TF-IDF vectorization.

 Built with:
- Python
- Scikit-learn
- Flask
- HTML/CSS (for UI)

---

## Features

 Train a spam classifier from a CSV  
 Clean and vectorize the email text  
 Flask web app for user interaction  
 Returns "SPAM" or "HAM" instantly

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Thoshani/email-spam-detector.git
cd email-spam-detector
2. Install Dependencies
pip install -r requirements.txt
3. Train the Model
python train_and_save.py
4. Run the Web App
python app.py
Open your browser at:
http://localhost:5000

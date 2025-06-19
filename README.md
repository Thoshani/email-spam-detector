# email-spam-detector
#  Email Spam Detection Web App

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

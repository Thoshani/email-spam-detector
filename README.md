# email-spam-detector
#  Email Spam Detection Web App


##  Project Code Availability

The **full source code** for the Email Spam Detection project is uploaded in this repository.

You can choose from **two options**:

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

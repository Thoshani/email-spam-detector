from flask import Flask, request, render_template
from spam_classifier import predict_spam

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form.get("email")
    result = predict_spam(email_text)
    return render_template("index.html", result=result, email=email_text)

if __name__ == '__main__':
    app.run(debug=True)

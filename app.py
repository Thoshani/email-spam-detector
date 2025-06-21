from flask import Flask, request, render_template
from spam_classifier import predict_spam

app = Flask(__name__)

@app.route('/')
def home():
    # Render the homepage with empty form
    return render_template("index.html", result=None, email=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input text from the form
    email_text = request.form.get("email")

    # Get prediction result: 'spam' or 'ham'
    result = predict_spam(email_text).lower()  # ensure lowercase for CSS class

    # Render the same page with prediction and email filled in
    return render_template("index.html", result=result, email=email_text)

if __name__ == '__main__':
    app.run(debug=True)
    



from flask import Flask, render_template, request
import pickle
import re
from nltk.corpus import stopwords

app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
except FileNotFoundError:
    print("Error: Model files not found! Run 'python model.py' first.")
    exit()

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_text = request.form["news"]
        cleaned = clean_text(user_text)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]
        
        if prediction == "fake":
            result = "⚠️ Caution: Likely Fake / Rumor"
        else:
            result = "✅ Safe: Likely Genuine News"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
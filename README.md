# 🛡️ RumorShield - Fake News Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Machine Learning](https://img.shields.io/badge/AI-Scikit%20Learn-orange)

## 📌 Project Overview
**RumorShield** is a Machine Learning-based web application designed to detect fake news and rumors. It uses **Natural Language Processing (NLP)** to analyze text (like WhatsApp forwards or news headlines) and classifies them as either **"Real"** or **"Fake"**.

## 🚀 Features
- **Instant Analysis:** Paste a message and get results in seconds.
- **Machine Learning:** Uses the *Multinomial Naive Bayes* algorithm for classification.
- **User-Friendly Interface:** Simple and clean Web UI.
- **Lightweight:** Runs locally on any laptop.

## 📂 Folder Structure
~~~text
RumorShield
│
├── app.py              # The Main Web Server (Flask)
├── model.py            # The Brain (Machine Learning Training Script)
├── fake_news.csv       # The Dataset (Examples of Real/Fake news)
├── model.pkl           # Saved Model (Created after running model.py)
├── vectorizer.pkl      # Saved Vectorizer (Created after running model.py)
│
├── templates
│   └── index.html      # The Website Frontend (HTML)
│
└── static
    └── style.css       # The Styling (CSS)
~~~

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, NLTK
* **Frontend:** HTML, CSS

---

## ⚙️ How to Run Locally

### 1. Install Required Libraries
Open your terminal (Command Prompt or VS Code Terminal) and run:
~~~bash
pip install flask pandas scikit-learn nltk
~~~

### 2. Train the Model
Before running the website, you must train the AI model once:
~~~bash
python model.py
~~~
*You will see a success message saying the model is saved.*

### 3. Start the Website
Run the Flask application:
~~~bash
python app.py
~~~

### 4. Open in Browser
Click the link in the terminal or go to:
~~~text
http://127.0.0.1:5000
~~~

---

## 🧪 Example Tests

**Try pasting these to test accuracy:**

1.  **Fake Example:**
    > "Forward this message to 10 people to win a free iPhone immediately!"

2.  **Real Example:**
    > "College will remain closed tomorrow due to heavy rain."

---

## 🔮 Future Scope
* Add a larger dataset for better accuracy.
* Add a "Report" button for users to flag incorrect results.

---
*Created by [Your Name]*
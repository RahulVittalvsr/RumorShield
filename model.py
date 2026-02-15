import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download stopwords (common words like 'the', 'is' that we ignore)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower() # Convert to lowercase
    text = re.sub(r'[^a-z\s]', '', text) # Remove special characters
    words = text.split()
    words = [w for w in words if w not in stop_words] # Remove stopwords
    return " ".join(words)

# 1. Load Data
try:
    data = pd.read_csv("fake_news.csv")
except FileNotFoundError:
    print("Error: fake_news.csv not found! Make sure it's in the same folder.")
    exit()

data["clean"] = data["text"].apply(clean_text)

# 2. Convert text to numbers (Vectorization)
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(data["clean"])
y = data["label"]

# 3. Train Model
model = MultinomialNB()
model.fit(X, y)

# 4. Save the brain (model)
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Success! Model trained and saved as model.pkl")
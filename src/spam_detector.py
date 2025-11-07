import streamlit as st
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Title
st.title("📧 Spam Email Detection App")

# Input text box
user_input = st.text_area("Enter the email text below:")

# Train a simple model (for demo purposes)
texts = [
    "Win a free iPhone now!",
    "Congratulations, you have been selected for a prize!",
    "Meeting scheduled for tomorrow at 10 AM.",
    "Please find attached the project report.",
    "You have won a $1000 Walmart gift card!",
    "Reminder: Submit your assignment by tonight."
]
labels = [1, 1, 0, 0, 1, 0]  # 1 = spam, 0 = not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# Predict if user input is spam or not
if st.button("Check Email"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        user_vector = vectorizer.transform([user_input])
        prediction = model.predict(user_vector)[0]
        if prediction == 1:
            s

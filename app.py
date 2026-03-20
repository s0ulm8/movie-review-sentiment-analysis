import streamlit as st
import joblib

# Load the saved model and vectorizer
# Make sure these filenames perfectly match the files you downloaded!
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

st.title("🎥 Movie Review Sentiment Analyzer")
st.write("Enter a movie review below to find out if it's Positive or Negative!")

# Text input for the user
user_input = st.text_area("Movie Review:")

if st.button("Predict Sentiment"):
    if user_input:
        # Transform the input using the saved vectorizer
        transformed_input = vectorizer.transform([user_input])
        
        # Make the prediction
        prediction = model.predict(transformed_input)
        
        # Display the output (Adjust the '1' if your positive label is different, e.g., 'positive')
        if prediction[0] == 1: 
            st.success("Positive Review! 🍿")
        else:
            st.error("Negative Review! 🍅")
    else:
        st.warning("Please enter a review first.")
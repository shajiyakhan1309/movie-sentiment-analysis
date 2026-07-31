import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb  #type:ignore
from tensorflow.keras.preprocessing import sequence    #type: ignore
from tensorflow.keras.models import load_model      #type: ignore

word_index=imdb.get_word_index()

reversed_word_index={value: key for key, value in word_index.items()}

# Load pre-trained model
model=load_model("simple_rnn_imdb.h5")

# Function to decode an encoded review 
# def decode_review(encoded_review):
#     """ 
#     Converts a list of integers (encoded review) back into the words.
#     """
#     return " ".join([reversed_word_index.get(i-3, "?") for i in encoded_review])


# Function to preprocess user input text
def preprocess_text(text):
    """ 
    Converts raw user text (a movie review) into a format that the RNN model can understand
    """
    words=text.lower().split()
    encoded_review=[word_index.get(word, 2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review], maxlen=200)
    return padded_review

# Function to predict sentiment of a given review
# def predict_sentiment(review):
#     """ 
#     Takes a text review, preprocesses it, and predicts sentiment
#     """
#     preprocessed_input=preprocess_text(review)
#     prediction=model.predict(preprocessed_input)
#     # if score>0.5: positive , else Negative
    
#     sentiment= "Positive" if prediction[0][0]>0.5 else "Negative"
#     return sentiment, prediction[0][0]

# Streamlit interface
st.title("IMDB Movie Review sentiment analysis")
st.write("Enter a movie review to classify it as 'positive' or 'negative' ")
user_input=st.text_area("Movie Review")

if st.button("Classify"):

    if not user_input.strip():
        st.warning("⚠️ Please enter a movie review.")
    else:
        try:
            preprocessed_input = preprocess_text(user_input)
            prediction = model.predict(preprocessed_input, verbose=0)

            score = float(prediction[0][0])
            sentiment = "Positive" if score > 0.5 else "Negative"

            st.success(f"Predicted Sentiment: {sentiment}")
            st.write(f"Confidence Score: {score:.4f}")

        except Exception:
            st.error(
                "Sorry! I couldn't analyze this review. "
                "Please try using simpler English words."
            )
        
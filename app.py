import streamlit as st
import tensorflow as tf
import pickle
from keras.layers import TFSMLayer

# Load model dari SavedModel
model = TFSMLayer("model_sequential", call_endpoint="serving_default")

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title("Hate Speech Detection")

text = st.text_area("Masukkan teks")

if st.button("Prediksi"):
    vectorized = vectorizer(tf.constant([text]))
    vectorized = tf.cast(vectorized, tf.float32)

    # Prediksi
    output_dict = model(vectorized)
    pred = list(output_dict.values())[0].numpy()[0][0]

    label = "Teks diatas mengandung Hate Speech" if pred > 0.5 else "Bukan Hate Speech"
    st.write(f"**{label}** (Confidence: {pred:.2f})")

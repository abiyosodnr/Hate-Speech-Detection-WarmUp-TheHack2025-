import joblib
import re

# --- Fungsi Preprocessing ---
def preprocess(text):
    text = text.encode('ascii', 'ignore').decode()
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = text.replace("url", '')
    text = re.sub(r'@\w+|\#','', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\brt\b', '', text)
    text = re.sub(r'user', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

# --- Load model & vectorizer ---
modelHS = joblib.load('modelHS.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# --- Program utama ---
while True:
    user_input = input("\nSilakan tulis komentar Anda: ")
    clean_text = preprocess(user_input)
    vectorized = vectorizer.transform([clean_text])
    predictionHS = modelHS.predict(vectorized)[0]

    if predictionHS == 1:
        print("🚫 Komentar Anda mengandung kalimat yang tidak diperkenankan. Silakan tulis komentar yang lebih baik.")
    else:
        print("✅ Komentar Anda diterima. Terima kasih!")
        break  # keluar dari loop jika komentar valid

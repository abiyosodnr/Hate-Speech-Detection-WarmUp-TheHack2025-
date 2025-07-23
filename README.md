# 🛡️ Hate Speech Detection - Warmup Project for The Hack 2025

This repository contains a machine learning project developed as a warmup before participating in **The Hack 2025**, an innovation program organized by **UKM CCI - Telkom University**. Our team is building a text classification system to detect **hate speech** using **Natural Language Processing (NLP)** techniques.

The project emphasizes end-to-end implementation — from text preprocessing to model evaluation — and is intended to strengthen our technical readiness ahead of the competition.

---

## 👥 Team Members

- Muhammad Al Abrar (Leader)  
- Abiyoso Danar Panji Yudhanto  
- Rizka Ananda Pratama

---

## 🎯 Objectives

- Build a text classification pipeline for hate speech detection  
- Apply NLP techniques for effective feature extraction  
- Train and evaluate multiple machine learning models  
- Use terminal interface for predictions and result display  
- Prepare foundational components for further development during The Hack 2025  

---

## 🧠 Methodology

### 1. Dataset

We use a labeled dataset containing text samples categorized into:
- Hate Speech  
- Offensive Language  
- Neutral  

### 2. Preprocessing

Text cleaning and preparation include:
- Lowercasing  
- Removing special characters and numbers  
- Stopword removal  
- Tokenization & Lemmatization  
- Normalization (slang conversion if necessary)  

### 3. Feature Extraction

We convert text into numerical representations using:
- TF-IDF Vectorization  
- (Optional) Bag-of-Words  

### 4. Model Training

Several machine learning models are tested:
- Logistic Regression  
- Naive Bayes  
- Support Vector Machine (SVM)
- Random Forest

### 5. Evaluation

We evaluate models using:
- Accuracy  
- Precision, Recall, F1-Score  
- Confusion Matrix  

---

## 💻 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/hate-speech-detection-warmup.git
cd hate-speech-detection-warmup

# Install dependencies
pip install -r requirements.txt

# Run the detection script
python main.py

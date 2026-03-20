# Movie Review Sentiment Analysis Project

## 📌 Project Overview
This project implements a Natural Language Processing (NLP) pipeline to classify movie reviews as either **Positive** or **Negative**. It includes a comparative analysis of multiple machine learning classification models and features a user-friendly Graphical User Interface (GUI) built with Streamlit.

## 🚀 Features
* **Text Preprocessing:** Vectorization of raw text data using TF-IDF.
* **Model Comparison:** Evaluated multiple classification models based on Accuracy, Precision, Recall, and F1-Score.
* **High-Accuracy Selection:** Deployed the best-performing model achieving **≥ 95% accuracy**.
* **Interactive GUI:** A Streamlit-based web application allowing users to input custom reviews and receive real-time sentiment predictions.

## 🛠️ Technologies & Libraries Used
* **Language:** Python
* **Machine Learning:** scikit-learn, pandas, numpy
* **Model Serialization:** joblib / pickle
* **GUI Framework:** Streamlit
* **Environment:** Google Colab (Training) / Local Windows (Deployment)

## 📂 Repository Contents
* `app.py`: The Streamlit application script for the GUI.
* `C2-24_SahilDeotale_NLP_Prac8.ipynb`: The original Google Colab notebook containing the complete code and explanation.
* `C2-24_SahilDeotale_NLP_Prac8.pdf`: Exported PDF version of the Colab notebook.
* `sentiment_model.pkl` & `tfidf_vectorizer.pkl`: The serialized high-accuracy model and text vectorizer. *(Note: If files were too large for GitHub, mention that they are stored locally instead).*

## 💻 How to Run the GUI Locally
To run this project on your own machine, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running:
   ```bash
   pip install streamlit scikit-learn

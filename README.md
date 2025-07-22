# 🫀 Heart Disease Risk Assessment Tool

A Machine Learning-powered web app that predicts an individual's risk of heart disease based on medical and lifestyle inputs. Designed with a user-friendly interface and built using real-world health data, this project showcases end-to-end development — from data preprocessing to model deployment.

## 📌 Objective

Build a smart UI where users can input health metrics and receive an instant prediction on their heart disease risk. This tool is designed to aid awareness and encourage timely medical attention.

## 🚀 Key Highlights

- 🔍 **Data Exploration & Cleaning**: Thorough preprocessing of health features such as chest pain, shortness of breath, blood pressure, cholesterol, and lifestyle habits.
- 🧠 **ML Model (Random Forest Classifier)**: Achieved **99.2% accuracy and f1-score** using a well-balanced and tuned classifier.
- 💡 **Feature Engineering**: Converted multiple binary medical indicators and continuous age data into model-ready formats.
- 🖥 **Streamlit UI**: Built an intuitive interface for real-time user interaction and prediction.
- ✅ **Confusion Matrix & Evaluation**: Validated using classification report and confusion matrix with over 14,000 test samples.

## 📊 Tech Stack

- **Python**
- **Pandas**, **NumPy**, **Scikit-learn**
- **Streamlit** for UI
- **Matplotlib / Seaborn** for optional data visualization
- **Joblib** for model serialization

## 📂 Dataset

- **Source**: [Heart Disease Risk Prediction Dataset](https://www.kaggle.com/datasets/mahatiratusher/heart-disease-risk-prediction-dataset?resource=download)  
- **Author**: Mahatir Ahmed Tusher  
- **Features**: 18 health-related input fields including symptoms, vitals, medical history, and age.

## 🧪 Model Performance

```text
Accuracy: 99.2%

Classification Report:
               precision    recall  f1-score   support
         0.0       0.99      0.99      0.99      6998
         1.0       0.99      0.99      0.99      7002

Confusion Matrix:
 [[6946   52]
  [  59 6943]]

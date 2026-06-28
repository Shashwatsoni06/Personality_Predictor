# 🧠 AI Personality Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?logo=scikitlearn)
![Classification](https://img.shields.io/badge/Machine_Learning-Classification-success)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-blue?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📖 Overview

The **AI Personality Prediction System** is an end-to-end Machine Learning application that predicts an individual's personality type based on behavioral traits.

Built using **Python**, **Scikit-learn**, and **Streamlit**, the application allows users to provide behavioral inputs through an interactive interface and instantly receive a predicted personality type along with the model's confidence score.

The project demonstrates practical implementation of machine learning classification, feature scaling, model serialization, and deployment through a modern web application.

---

# ✨ Features

- 🧠 Predict personality type instantly
- 📊 Displays prediction confidence
- 🎛️ Dynamic feature generation from trained model
- ⚡ Real-time prediction
- 📱 Clean and responsive Streamlit interface
- 🔄 Automatic feature scaling
- 🤖 Machine Learning-powered classification

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Project Type | Multi-Class Classification |
| Data Processing | Pandas |
| Model Serialization | Pickle |
| Web Framework | Streamlit |

---

# 📂 Project Structure

```text
Personality_Predictor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── personality_model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── model_features.pkl
│
└── .devcontainer/
    └── devcontainer.json
```

---

# 📊 Model Inputs

The application dynamically loads all model features from `model_features.pkl`.

Users provide behavioral scores using intuitive sliders, and the interface automatically matches the expected feature order used during training.

---

# ⚙️ How It Works

1. User provides behavioral trait scores.
2. Input values are converted into a DataFrame.
3. Features are arranged in the exact order used during training.
4. The StandardScaler transforms the input data.
5. The trained classification model predicts the personality type.
6. The Label Encoder converts the prediction back to a readable class.
7. The confidence score is calculated using the model's probability estimates.

---

# 🧠 Machine Learning Pipeline

### Data Preprocessing

- Feature Selection
- Feature Scaling using StandardScaler
- Label Encoding

### Model Prediction

The trained classification model predicts the user's personality type.

The application also displays the prediction confidence using `predict_proba()`.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Shashwatsoni06/Personality_Predictor.git
```

## Navigate to Project

```bash
cd Personality_Predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

# 📦 Dependencies

- Streamlit
- Pandas
- Scikit-learn

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 📸 Application Preview

## 🏠 Home Screen

> <img width="2866" height="1432" alt="image" src="https://github.com/user-attachments/assets/0e0818c9-aa71-4fa1-9f00-24c537e3e6e4" />


---

## 🎯 Prediction Result

> <img width="2868" height="1420" alt="image" src="https://github.com/user-attachments/assets/e3430334-ab1a-4e05-92f9-0bee53d87cde" />


---

# 💡 Learning Outcomes

This project helped me gain practical experience in:

- Multi-Class Classification
- Feature Scaling
- Label Encoding
- Dynamic Feature Handling
- Model Serialization with Pickle
- Confidence Score Estimation
- Streamlit Deployment
- End-to-End Machine Learning Application Development

---

# 🔮 Future Improvements

- Personality trait visualization
- Explainable AI (SHAP/LIME)
- Multiple model comparison
- Personality report generation
- REST API deployment
- Cloud deployment (AWS, Render, Hugging Face)
- User authentication
- Historical prediction dashboard

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# 👨‍💻 Author

**Shashwat Soni**

- 💼 LinkedIn: https://www.linkedin.com/in/shashwat-soni/
- 💻 GitHub: https://github.com/Shashwatsoni06

Live Demo: https://personalitypredictor-crh2wjviei9qtpvqv3crfm.streamlit.app/

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

<p align="center">

**Built with ❤️ using Python, Scikit-learn, Machine Learning & Streamlit**

</p>

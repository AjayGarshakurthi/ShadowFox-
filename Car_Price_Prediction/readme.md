# 🚗 Car Price Prediction Using Machine Learning

## 📌 Overview

This project predicts the selling price of a used car based on various features such as present price, kilometers driven, fuel type, seller type, transmission type, number of previous owners, and car age.

The model is built using Machine Learning and deployed as an interactive web application using Streamlit.

---

## 🎯 Problem Statement

Estimating the selling price of a used car can be difficult due to multiple factors affecting its value. This project uses Machine Learning techniques to predict car prices accurately based on historical data and vehicle attributes.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## 📊 Dataset Features

* Present Price
* Kilometers Driven
* Number of Previous Owners
* Car Age
* Fuel Type
* Seller Type
* Transmission Type

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Splitting
6. Model Selection
7. Model Training
8. Model Evaluation
9. Deployment

---

## 🤖 Model Used

**Random Forest Regressor**

Reason for selection:

* High prediction accuracy
* Handles non-linear relationships effectively
* Robust against overfitting

---

## 🚀 Live Demo

🔗 **Live Application:**
https://cytohcjwsd8w8h2zzygq2t.streamlit.app/
---

## 📂 Project Structure

```text
Car_Price_Prediction/
│
├── app.py
├── car_price_model.pkl
├── car.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ▶️ How to Run Locally

### Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Sample Prediction

Input:

* Present Price = 5 Lakhs
* Kilometers Driven = 30000
* Owners = 0
* Fuel Type = Petrol
* Seller Type = Dealer
* Transmission = Manual
* Car Age = 5 Years

Output:

* Estimated Selling Price = ₹3.31 Lakhs

---

## 🔮 Future Enhancements

* Improve model accuracy with advanced algorithms
* Add more vehicle features
* Deploy using cloud platforms
* Enhance UI design

---

## 👨‍💻 Author

Ajay Garshakurthi

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

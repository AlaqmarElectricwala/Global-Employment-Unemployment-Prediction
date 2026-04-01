# 📊 Employment & Unemployment Prediction (ML Project)

## 🚀 Project Overview

This project uses **Machine Learning (Linear Regression)** to predict future **employment** and **unemployment rates** based on historical global data.

The model learns patterns from past years and estimates future trends using a simple and interpretable approach.

---

## 🎯 Objective

* Predict **employment rate 📈**
* Predict **unemployment rate 📉**
* Use only **year as input**
* Build a **beginner-friendly ML pipeline**

---

## 📂 Dataset

The dataset contains global labor statistics with the following files:

* `occupazione.csv` → Employment data
* `disoccupazione.csv` → Unemployment data

### Key Columns:

* `country` → Country name
* `year` → Year
* `sex` → Gender category
* `age` → Age group
* `obs_value` → Rate value

---

## 🧹 Data Preprocessing

Steps performed:

* Filtered data for:

  * `sex = Total`
  * `age = 15+`
* Merged both datasets on:

  * `country`
  * `year`
* Sorted data for consistency

---

## 🤖 Machine Learning Model

We use:

* **Linear Regression**

### Input (Feature):

* `year`

### Output (Targets):

* Employment rate
* Unemployment rate

Two separate models are trained:

* Model 1 → Employment prediction
* Model 2 → Unemployment prediction

---

## ⚙️ How It Works

1. Load datasets
2. Clean and filter data
3. Merge employment & unemployment data
4. Train Linear Regression models
5. Take user input (year)
6. Predict future rates

---

## 🧪 Example

### Input:

```
Enter year to predict employment and unemployment rates: 2025
```

### Output:

```
For year 2025:
Employment Rate: 56.43%
Unemployment Rate: 7.33%
```

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas 📊
* Scikit-learn 🤖

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/employment-unemployment-prediction.git
```

2. Navigate to the project folder:

```
cd employment-unemployment-prediction
```

3. Install dependencies:

```
pip install pandas scikit-learn
```

4. Run the script:

```
python main.py
```

---

## ⚠️ Limitations

* Uses only **year as input** (no economic indicators)
* Assumes **linear trend**
* Predictions are **approximate**, not exact

---

## 🚀 Future Improvements

* Add **country-based prediction 🌍**
* Include **more features** (GDP, population, etc.)
* Add **data visualization 📊**
* Build a **web app interface**
* Use advanced models (Random Forest, XGBoost)

---

## 💡 Key Learning Outcomes

* Data cleaning & preprocessing
* Merging datasets
* Feature selection
* Training ML models
* Making predictions
* Handling real-world datasets

---

## 👨‍💻 Author

* Your Name

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---

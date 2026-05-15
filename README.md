# Salary Prediction Using Simple Linear Regression

## Project Overview

This project is a Machine Learning application developed to predict employee salary based on years of experience using the Simple Linear Regression algorithm. The project demonstrates the complete workflow of a Machine Learning model, including:

- Data collection and preprocessing
- Exploratory analysis
- Model training
- Model serialization
- Deployment using Streamlit

The application allows users to enter years of experience and instantly receive a predicted salary value.

---

## Project Structure

```text
Salary-Prediction-Project/
│
├── 01_Salary_Prediction_Model.ipynb
├── 02_Model_Deployment.ipynb
├── app.py
├── Salary_Data.csv
├── finalized_model.sav
├── requirements.txt
└── README.md
```

---

## Technologies Used

| Category | Tools / Libraries |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Analysis | Pandas |
| Data Visualization | Matplotlib |
| Model Deployment | Streamlit |
| Model Serialization | Pickle |

---

## Dataset Information

The dataset contains the following columns:

| Feature | Description |
|---|---|
| YearsExperience | Number of years of professional experience |
| Salary | Salary corresponding to the experience |

---

## Machine Learning Workflow

### 1. Import Required Libraries

The project uses standard Python libraries for:
- Data handling
- Visualization
- Model training
- Deployment

### 2. Load Dataset

The dataset is loaded using Pandas and analyzed for:
- Missing values
- Data types
- Data distribution

### 3. Feature Selection

- Input Feature:
  - `YearsExperience`

- Target Variable:
  - `Salary`

### 4. Model Training

The model is trained using:

```python
Simple Linear Regression
```

The regression model learns the relationship between:
- Years of experience
- Salary growth

### 5. Model Saving

The trained model is serialized and saved as:

```text
finalized_model.sav
```

### 6. Deployment

The project is deployed using Streamlit to provide an interactive web interface.

---

## Streamlit Application

The Streamlit application allows users to:

- Enter years of experience
- Predict salary instantly
- Interact with the trained ML model through a user-friendly interface

### Application Input

```text
Years of Experience
```

### Application Output

```text
Predicted Salary
```


## Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Model Prediction Example

| Years of Experience | Predicted Salary |
|---|---|
| 2.0 | 45,508.08 |
| 5.5 | 78,218.88 |
| 10.0 | 120,275.62 |

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Supervised Machine Learning
- Linear Regression
- Data preprocessing
- Model deployment
- Building ML web applications
- Streamlit integration
- Model serialization using Pickle

---

## Future Improvements

Possible enhancements for this project:

- Add advanced regression models
- Improve UI design
- Deploy on cloud platforms
- Add model evaluation metrics
- Add visualization dashboard
- Support multiple input features

---

## Author

**MANIKANDAPRABHU.S**

Machine Learning and Artificial Intelligence Enthusiast



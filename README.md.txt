# Salary Prediction using Simple Linear Regression

Author: Manikandaprabhu.S  
Project Type: Machine Learning – Regression

## Project Overview

This project predicts salary based on years of experience using a Simple Linear Regression model implemented with Scikit-Learn.

The objective is to understand the relationship between years of experience and salary and build a regression model to make predictions.

## Dataset

File used: Salary_Data.xls

The dataset contains two columns:

- YearsExperience (Independent Variable)
- Salary (Dependent Variable)

## Workflow

1. Import required libraries
2. Load dataset using pandas
3. Prepare feature variable (X) and target variable (y)
4. Split dataset into training and testing sets
5. Train Linear Regression model
6. Make predictions on test data
7. Evaluate model using R² Score and Mean Squared Error
8. Visualize regression results using Matplotlib
9. Save trained model using pickle

## Model Evaluation

The model performance is evaluated using:

- R² Score
- Mean Squared Error (MSE)

The results indicate a strong positive linear relationship between years of experience and salary.

## Project Files

- 01_Salary_Prediction_Model.ipynb – Model training and evaluation
- 02_Model_Deployment.ipynb – Loading saved model and making predictions
- finalized_model.sav – Trained regression model
- Salary_Data.xls – Dataset used for training
- requirements.txt – Required Python libraries

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-Learn
- Pickle

## Model Usage

The saved model can be loaded and used for prediction:

```python
import pickle

model = pickle.load(open('finalized_model.sav', 'rb'))
prediction = model.predict([[5]])
print(prediction)
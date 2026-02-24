# Salary Prediction using Simple Linear Regression



### Author: MANIKANDAPRABHU.S

#### Project Type: Machine Learning – Regression





#### **1)Project Overview**



* ##### This project predicts salary based on years of experience using a Simple Linear Regression model implemented with Scikit-Learn.



* ##### The objective is to understand the relationship between years of experience and salary and build a regression model to make predictions.





#### **2)Dataset**



##### File used: Salary\_Data.xls

##### The dataset contains two columns:

* ###### YearsExperience (Independent Variable)
* ###### Salary (Dependent Variable)





#### **3)Workflow**



* ##### Import required libraries
* ##### Load dataset using pandas
* ##### Prepare feature variable (X) and target variable (y)
* ##### Split dataset into training and testing sets
* ##### Train Linear Regression model
* ##### Make predictions on test data
* ##### Evaluate model using R² Score and Mean Squared Error
* ##### Visualize regression results using Matplotlib
* ##### Save trained model using pickle





#### **4)Model Evaluation**



* ###### The model performance is evaluated using:
* ###### R² Score (0.9749154407708353)
* ###### Mean Squared Error (MSE : 21026037.329511296)

##### The results indicate a strong positive linear relationship between years of experience and salary.





#### **5)Project Files**



* ###### **01\_Salary\_Prediction\_Model.ipynb** – (Model training and evaluation)
* ###### **02\_Model\_Deployment.ipynb** – (Loading saved model and making predictions)
* ###### **finalized\_model.sav** – (Trained regression model)
* ###### **Salary\_Data.xls** – (Dataset used for training)
* ###### **requirements.txt** – (Required Python libraries)





#### **6)Technologies Used**



* ###### Python
* ###### Pandas
* ###### Matplotlib
* ###### Scikit-Learn
* ###### Pickle

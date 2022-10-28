# IoT-Device-Type-Identification-Using-Machine-Learning
For the IoT device type identification, this project was intended to test Extreme Gradient Boosting Classifier (XGBoost Classifier) to determine the model in terms of accuracy on testing and validation data.

## Dataset
The dataset for this project is available at shorturl.at/nqY08. It consists 298 columns and 1000 rows.

## Training and Testing the ML Algorithms
The dataset will be divided into eighty percent (80%) training sets and twenty percent (20%) validation sets.

## Data Preprocessing
The data of different IoT device types will undergo to data preprocessing. Since the dataset has 298 features, I’ve used XGBoost feature importance to know which features have a larger effect on the model.

# Results

## 1. Feature Importance
### a. Top 5 most and least important features
![image](https://user-images.githubusercontent.com/22261606/198205722-13c38ad6-2293-4e14-8aff-8a0ab2180ffa.png)
### b. Feature Importance Obtain from Coefficients
![image](https://user-images.githubusercontent.com/22261606/198205786-8409c076-135a-4e6c-ad3c-7dbf08b622cc.png)
### c. c.	Cumulative Explained Variance by Number of Principal Components
![image](https://user-images.githubusercontent.com/22261606/198205832-1ae366a9-7dcc-4dd1-b2ab-71b6a0ce3e85.png)

## 2. Extreme Gradient Boosting Classifier Model (XGBoost Classifier)
The experimental results demonstrate that XGBoost Classifier model has an accuracy of 95.00% on training data and 81.00% on validation data. The model performs well in terms of accuracy. It has been found that this demo’s functionalities are working as intended.

![image](https://user-images.githubusercontent.com/22261606/198205939-eae728a0-a840-4037-ba70-4d67e13353c6.png)

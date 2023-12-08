# Food Service Delivery - Prediction of the Time Taken to Make the Delivery
This is a machine learning project focused on providing a satisfactory approximation of the time taken to make a food delivery, in minutes, for a food delivery company. Having a prediction of the time it will take for your delivery to reach your location after it leaves the restaurant is a very important feature to have regarding customer service. 
#
![image](https://github.com/T1burski/delivery_time_prediction/assets/100734219/dcc8f072-1d48-4a59-b66f-7aeb6c6a7f71)
## 1) The Problem
As a data scientist, we received the challenge to develop a machine learning model that predicts the time that a delivery will take, in minutes, after the delivery person leaves the restaurant until they reach the client's location. Also, after developing the model, we need to deploy it in a web app with which a user from the food delivery company can test the results applying different delivery conditions.

The food delivery company stated that, for now, they don't needa model that gives the exact prediction of the time it will take to make the delivery, but a satisfactory estimate. The company is new and does not have much data, hence the not so big necessity to have amazing results by now.

## 2) The Data
The data provided by the company is formed by the following information:

- ID - Delivery Identification (string)

- Delivery_person_ID - Identification code of the person that made the delivery (string)

- Delivery_person_Age - The age of the person that made the delivery (integer)

- Delivery_person_Ratings - Numeric rating of the person that made the delivery informed by previous clients (float)

- Restaurant_latitude - Numeric global orientation number representing the latitude of the restaurant's location (float)

- Restaurant_longitude - Numeric global orientation number representing the longitude of the restaurant's location (float)

- Delivery_location_latitude - Numeric global orientation number representing the latitude of the client's location (float)

- Delivery_location_longitude - Numeric global orientation number representing the longitude of the client's location (float)

- Type_of_order - Type of food ordered (drinks, buffet...) (string)

- Type_of_vehicle - Type of vehicle used to make the delivery (motorcycle, bycicle...) (string)

- Time_taken(min) - Time taken, in minutes, to make the delivery: go from the restaurant's location to the client's location (float)

We were given a relatively small dataset (45593 rows) that represent previous deliveries made by the company in a city.

## 3) Technologies That Help us Solve the Problem
We have in our hands a Supervised Regression problem. Using a conda virtual enviroment, we develop the model using Visual Studio Code with Python language with various libraries such as Pandas, Numpy, XGBoost and SKLearn. Finally, we deply our model in a web app made with Streamlit.
![image](https://github.com/T1burski/delivery_time_prediction/assets/100734219/87aef6b4-5358-48dc-8d85-a79361e2ef39)

## 3) Exploring and Building the Solution
All details regarding exploratory data analysis, hypothesis, statiscal findings, feature selection, model selection and model hyperparameter tuning are fully documented and explained on the eda.ipynb file within the notebook folder of the project.

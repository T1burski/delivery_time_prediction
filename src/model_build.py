from data_ingestion import DataIngestion
from data_preprocessing import DataPreprocessor
from feature_standarization import FeatureStandardizer
from feature_engineering import FeatureEngineering
from model_training import ModelTrainer
import pickle
import pandas as pd
import numpy as np

'''
this script adds together all modules in a pipeline to ingest
and transform the data so, afterwards, we train the model.
'''

data_source = "data\deliverytime.csv"

data = DataIngestion(data_path=data_source).load_data()

engineered_data = FeatureEngineering(data).engineer()

processed_data = DataPreprocessor(engineered_data).preprocess()

X_features = ['Delivery_person_Age', 'Delivery_person_Ratings', 'is_motorcycle', 'Delivery_Distance_km']

y_target = ['Time_taken(min)']

X_data = processed_data[X_features]

y_data = processed_data[y_target]

standardizer = FeatureStandardizer(X_features).fit(X_data)

X_data_standardized = standardizer.transform(X_data)

model = ModelTrainer().train_model(X_data_standardized, y_data.values.ravel())

'''
after all steps of the pipeline were made, we save the model and the
feature standardizer in pickle files inside the artifacts folder within
te project so they can be used later on when transforming and predicting
new data with the ML Web App
'''

with open('artifacts\model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('artifacts\standardization.pkl', 'wb') as standardization_file:
    pickle.dump(standardizer, standardization_file)
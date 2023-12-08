import pandas as pd
from xgboost import XGBRegressor

'''
module created to train the XGBoost model using the hyperparameters
obtained after CV GridSearch tuning
'''

class ModelTrainer:
    def __init__(self):
        '''
        defines the hyperparameters (4)
        '''
        params = {
                'eta': 0.2,
                'gamma': 10,
                'lambda': 2,
                'max_depth': 6
            }

        self.model = XGBRegressor(**params)
    
    def train_model(self, X, y):
        '''
        does the model fit (train), returning the trained model
        '''
        return self.model.fit(X, y)
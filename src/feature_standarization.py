import pandas as pd
from sklearn.preprocessing import StandardScaler

'''
module created to standardize the numeric features before inputing 
them in the model training and prediction
'''

class FeatureStandardizer:
    def __init__(self, features):
        self.features = features
        self.scaler = StandardScaler()

    def fit(self, X_train):
        '''
        creates the fit method using StandardScaler from sklearn
        '''
        standardizer = self.scaler.fit(X_train[self.features])
        return standardizer
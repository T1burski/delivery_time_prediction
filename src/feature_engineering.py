import pandas as pd
import numpy as np
import math
from math import radians, sin, cos, sqrt, tan, atan2, exp

'''
module created to engineer the data. This engineering process is associated with
creating the distance feature by comparing the restaurant's and the client's longitude and latitude.
inside this module we also create the binary feature related to the vehicle used: if it was a motorcycle,
return 1, if it was not, return 0.
'''

class FeatureEngineering:
    def __init__(self, data):
        self.engineered_data = data

    def distance_calc(self, Rest_Lat, Rest_Lon, Dest_Lat, Dest_Lon):
        '''
        creates the function that calculates the distance
        '''
        R = 6373.0

        lat1 = radians(Rest_Lat)
        lon1 = radians(Rest_Lon)
        lat2 = radians(Dest_Lat)
        lon2 = radians(Dest_Lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def create_distances(self):
        '''
        uses the previously created function to actually create the distance feature, in km.
        '''
        self.engineered_data['Delivery_Distance_km'] = self.engineered_data.apply(lambda x: self.distance_calc(x.Restaurant_latitude, x.Restaurant_longitude, x.Delivery_location_latitude, x.Delivery_location_longitude), axis=1)

    def create_is_motorcycle_column(self):
        '''
        creates the feature indicating if the vehicle used was a
        motorcycle or not
        '''
        self.engineered_data["is_motorcycle"] = np.where(self.engineered_data["Type_of_vehicle"].str.contains("motorcycle"), 1, 0)

    def engineer(self):

        self.create_distances()

        self.create_is_motorcycle_column()

        return self.engineered_data
import pandas as pd
import numpy as np
import math

'''
module created to preprocess the data. This preprocessing is associated with
removing outliers by using statistical techniques applied to a auxiliary variable
that is given by the ratio between the time taken to make the delivery and the distance
of that same delivery.
'''


class DataPreprocessor:
    def __init__(self, data):
        self.raw_data = data
        self.processed_data = None

    def select_columns(self):
        selected_columns = ['Delivery_person_Age', 'Delivery_person_Ratings', 'is_motorcycle', 'Time_taken(min)', 'Delivery_Distance_km']
        self.processed_data = self.raw_data[selected_columns]

    def create_new_column(self):
        '''
        creating the auxiliary variable
        '''
        self.processed_data['time_over_dist'] = self.processed_data['Time_taken(min)'] / self.processed_data['Delivery_Distance_km']

    def outliers_limits(self, col):
        '''
        using the auxiliary variable to remove outliers
        '''
        def medcouple_generator(data, chunk_size=9**9999):
            for chunk in range(0, len(data), chunk_size):
                yield data[chunk:chunk + chunk_size]

        def calculate_medcouple(data):
            deviations = np.abs(data - np.median(data))
            q75, q25 = np.percentile(deviations, [75, 25])
            medcouple = (q75 - q25) / (q75 + q25)

            return medcouple

        data_generator = medcouple_generator(col.values)
        medcouple_values = []
    
        for chunk in data_generator:
            medcouple_values.append(calculate_medcouple(chunk))

        final_medcouple = np.median(medcouple_values)
        if final_medcouple >= 0:
            lower_bound = np.percentile(col, 25) - 1.5*(math.exp(-4*final_medcouple))*(np.percentile(col, 75) - np.percentile(col, 25))
            upper_bound = np.percentile(col, 75) + 1.5*(math.exp(3*final_medcouple))*(np.percentile(col, 75) - np.percentile(col, 25))
        else:
            lower_bound = np.percentile(col, 25) - 1.5*(math.exp(-3*final_medcouple))*(np.percentile(col, 75) - np.percentile(col, 25))
            upper_bound = np.percentile(col, 75) + 1.5*(math.exp(4*final_medcouple))*(np.percentile(col, 75) - np.percentile(col, 25))
        return lower_bound, upper_bound

    def remove_outliers(self):
        '''
        the previous function returns two boundaries: if the value of time/distance is lower
        than the lower bound or higher than the upper bound, it is considered a potential outlier
        and is, therefore, removed (filtered out)
        '''
        lower_bound, upper_bound = self.outliers_limits(self.processed_data['time_over_dist'])
        self.processed_data = self.processed_data.loc[(self.processed_data['time_over_dist'] > lower_bound) & (self.processed_data['time_over_dist'] < upper_bound)]

    def drop_column(self):
        self.processed_data = self.processed_data.drop(['time_over_dist'], axis=1)

    def preprocess(self):
        self.select_columns()

        self.create_new_column()

        self.remove_outliers()

        self.drop_column()

        return self.processed_data
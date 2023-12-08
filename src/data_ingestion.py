import pandas as pd

'''
module created to ingest the data. which in this case is a .csv file.
if the data source changes in the future, for example if we start consuming it through a cloud
service such as AWS, GCP or Azure, this is where we would change the data ingestion mode.
'''

class DataIngestion:
    def __init__(self, data_path):
        self.data_path = data_path
        
    def load_data(self):
        '''
        the path of the data, in this case located within the projects' data folder, is passed
        so we convert it to pandas format, returning it
        '''
        try:
            data = pd.read_csv(self.data_path)
            return data
        except FileNotFoundError:
            print("Error: File not found.")
            return None

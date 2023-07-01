import pandas as pd
from loguru import logger
from rich.progress import track


class DataPreprocessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.load_data()
        self.cleaned_data = self._clean_data()
        
    def load_data(self):
        logger.info(f"Loading data from {self.data_path}...")
        data = pd.read_csv(self.data_path)
        logger.info("Data loaded successfully!")
        return data

    def _clean_data(self):
        logger.info("Cleaning data...")
        for _ in track(range(100), description="Cleaning..."):
            cleaned_data = self.data['Longitude;Latitude'].str.split(';', n=-1, expand=True)
            cleaned_data = cleaned_data.rename(columns={0:'Lat', 1:'Long'})
            cleaned_data = cleaned_data.astype('float')
        logger.info("Data cleaned successfully!")
        return cleaned_data

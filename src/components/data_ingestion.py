import os
from kaggle.api.kaggle_api_extended import KaggleApi
from src.config import DataConfig


class DataIngestion:

    def __init__(self, config: DataConfig):
        self.config = config

    def download_data(self):

        api = KaggleApi()
        api.authenticate()

        os.makedirs(self.config.download_dir, exist_ok=True)

        api.dataset_download_files(
            self.config.data_url.split("datasets/")[-1],
            path=self.config.download_dir,
            unzip=True
        )
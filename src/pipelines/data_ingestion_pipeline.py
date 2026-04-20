from src.config import DataConfig
from src.components.data_ingestion import DataIngestion

config = DataConfig()

data_ingestion = DataIngestion(config)
data_ingestion.download_data()
from src.config import DataPreprocessingConfig
from src.components.data_preprocessing import DataPreprocessing


def run_data_preprocessing():

    config = DataPreprocessingConfig()

    data_preprocessing = DataPreprocessing(config)

    data_preprocessing.run_preprocessing()


if __name__ == "__main__":
    run_data_preprocessing()
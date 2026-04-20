from dataclasses import dataclass

import os

@dataclass
class DataConfig:
    data_url: str = "https://www.kaggle.com/datasets/spscientist/students-performance-in-exams"
    download_dir: str = "data"
    file_name: str = "StudentsPerformance.csv"




@dataclass
class DataPreprocessingConfig:
    
    root_dir: str = "artifacts/data_preprocessing"
    
    input_data_path: str = os.path.join("data", "StudentsPerformance.csv")
    
    processed_data_path: str = os.path.join(root_dir, "processed_data.csv")
    
    preprocessor_object_path: str = os.path.join(root_dir, "preprocessor.pkl")
    
    target_column: str = "average_score"
    
    columns_to_drop: list = None
    
    categorical_columns: list = None

    def __post_init__(self):
        self.columns_to_drop = [
            "math score",
            "reading score",
            "writing score"
        ]

        self.categorical_columns = [
            "gender",
            "race/ethnicity",
            "parental level of education",
            "lunch",
            "test preparation course"
        ]
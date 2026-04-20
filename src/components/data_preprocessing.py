import os
import pandas as pd
import pickle

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

from src.config import DataPreprocessingConfig


class DataPreprocessing:

    def __init__(self, config: DataPreprocessingConfig):
        self.config = config


    def run_preprocessing(self):

        # Load dataset
        df = pd.read_csv(self.config.input_data_path)

        # Create target column
        df[self.config.target_column] = (
            df["math score"] +
            df["reading score"] +
            df["writing score"]
        ) / 3

        # Split X and y
        X = df.drop(columns=self.config.columns_to_drop + [self.config.target_column])
        y = df[self.config.target_column]

        # Encoder
        encoder = OneHotEncoder(
            sparse_output=False,
            handle_unknown="ignore"
        )

        # Column transformer
        preprocessor = ColumnTransformer(
            transformers=[
                ("encoder", encoder, self.config.categorical_columns)
            ],
            remainder="passthrough"
        )

        # Transform features
        X_processed = preprocessor.fit_transform(X)

        # Feature names
        encoded_features = preprocessor.named_transformers_[
            "encoder"
        ].get_feature_names_out(self.config.categorical_columns)

        processed_df = pd.DataFrame(
            X_processed,
            columns=encoded_features
        )

        # Add target
        processed_df[self.config.target_column] = y.values

        # Create directory
        os.makedirs(self.config.root_dir, exist_ok=True)

        # Save preprocessor
        with open(self.config.preprocessor_object_path, "wb") as f:
            pickle.dump(preprocessor, f)

        # Save processed data
        processed_df.to_csv(self.config.processed_data_path, index=False)

        print("Data preprocessing completed")
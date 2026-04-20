import os
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


class ModelTrainer:

    def __init__(self, processed_data_path, model_output_path):
        self.processed_data_path = processed_data_path
        self.model_output_path = model_output_path


    def train_model(self):

        # Load processed dataset
        df = pd.read_csv(self.processed_data_path)

        # Split features and target
        X = df.drop(columns=["average_score"])
        y = df["average_score"]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Model
        model = LinearRegression()

        # Train
        model.fit(X_train, y_train)

        # Prediction
        predictions = model.predict(X_test)

        # Evaluation
        score = r2_score(y_test, predictions)
        print("Model R2 Score:", score)

        # Create directory if needed
        os.makedirs(os.path.dirname(self.model_output_path), exist_ok=True)

        # Save model
        with open(self.model_output_path, "wb") as f:
            pickle.dump(model, f)

        print("Model saved successfully")
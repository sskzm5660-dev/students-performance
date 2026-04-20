from src.components.model_trainer import ModelTrainer


def run_model_trainer():

    processed_data_path = "artifacts/data_preprocessing/processed_data.csv"
    model_output_path = "artifacts/model_trainer/student_model.pkl"

    trainer = ModelTrainer(
        processed_data_path,
        model_output_path
    )

    trainer.train_model()


if __name__ == "__main__":
    run_model_trainer()
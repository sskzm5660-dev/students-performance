import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(message)s:')

project_name = "my_project"

list_of_files = [

    ".github/workflows/.gitkeep",

    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/pipelines/__init__.py",
    f"src/utils/__init__.py",

    f"src/components/data_ingestion.py",
    f"src/components/data_validation.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",

    f"src/pipelines/training_pipeline.py",
    f"src/pipelines/prediction_pipeline.py",

    f"src/utils/logger.py",
    f"src/utils/exception.py",
    f"src/utils/helper.py",

    f"src/config.py",
    f"src/constants.py",

    "main.py",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore"
]


for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as f:
            pass

        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
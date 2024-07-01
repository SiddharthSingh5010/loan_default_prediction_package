import sys
import os 
from pathlib import Path

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))


from prediction_model.config import config
import pandas as pd
import numpy as np
from prediction_model.processing.data_handling import load_dataset,save_pipeline
from prediction_model.processing import preprocessing
import prediction_model.pipeline as pipe


def perform_training():
    train_data = load_dataset(file_name=config.TRAIN_FILE)
    train_y = train_data[config.TARGET].map({'N':0,'Y':1})
    pipe.classification_pipeline.fit(train_data[config.FEATURES],train_y)
    save_pipeline(pipeline_to_save=pipe.classification_pipeline)

if __name__ == '__main__':
    perform_training()

import sys
import os 
from pathlib import Path
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from sklearn.pipeline import Pipeline
from prediction_model.processing import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

classification_pipeline = Pipeline(
    [
        ('mean_imputation',preprocessing.MeanImputer(variables=config.NUM_FEATURES)),
        ('mode_imputation',preprocessing.ModeImputer(variables=config.CAT_FEATURES)),
        ('domain_processing',preprocessing.DomainProcessing(variable_to_add=config.FEATURES_TO_ADD,variable_to_modify=config.FEATURES_TO_MODIFY)),
        ('drop_features',preprocessing.DropColumns(variables_to_drop=config.DROP_FEATURES)),
        ('label_encoder',preprocessing.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
        ('log_transform',preprocessing.LogTransformer(variables=config.LOG_FEATURES)),
        ('min_max_scalaer',MinMaxScaler()),
        ('logistic_regression',LogisticRegression(random_state=0))
    ]
)
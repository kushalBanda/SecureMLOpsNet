from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging

from NetworkSecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from NetworkSecurity.entity.config_entity import DataValidationConfig
from NetworkSecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from utils.main_utils.utils import read_yaml_file

import os 
import sys
import numpy as np
import pandas as pd
from scipy.stats import ks_2samp

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataValidationArtifact,
                data_validation_config: DataValidationConfig):
        
        try:
            self.data_ingestion_artifact = DataIngestionArtifact
            self.data_validation_config = DataValidationConfig
            self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            # Read the data from train and test
            train_dataframe = DataValidation.initiate_data_validation()
            test_dataframe = DataValidation.initiate_data_validation()
        except Exception as e:
            raise NetworkSecurityException(e, sys)
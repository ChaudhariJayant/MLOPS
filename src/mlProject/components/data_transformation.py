
import os
from src.mlProject.entity.config_entity import DataTransformationConfig
from src.mlProject import logger
import pandas as pd
from sklearn.model_selection import train_test_split



class DataTransformation:
    
    def __init__ (self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir ,"train.csv"), index = False) 
        test.to_csv(os.path.join(self.config.root_dir , "test.csv"), index = False)

        logger.info(f"Train and Test data saved in {self.config.root_dir}")
        logger.info(f"Train data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")

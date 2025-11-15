from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject import logger
import pandas as pd
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:    
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split()[-1]
            
            if status == "True":
                try:
                    config= ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_tansformation = DataTransformation(config = data_transformation_config)
                    data_tansformation.train_test_spliting()
                except Exception as e:
                    raise e
            else:
                raise Exception(" Invalid Schema")
        except Exception as e:
            raise e
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject import logger
import pandas as pd
from pathlib import Path

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __int__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config= ModelTrainer(config= model_trainer_config)
            model_trainer_config.train()
            logger.info("------ Model Training completed----------")

        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
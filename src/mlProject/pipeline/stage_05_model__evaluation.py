from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_evaluation import ModelEvaluation
from src.mlProject import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(sellf):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


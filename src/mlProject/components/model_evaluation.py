import os 
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.mlProject.entity.config_entity import ModelEvaluationConfig
from src.mlProject.utils.common import save_json
from pathlib import Path



class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        rsme = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rsme, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[[self.config.target_column]]

        # mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        # logger.info(f"url fuck up {urlparse(mlflow.get_tracking_uri())}")
        

        with mlflow.start_run():
            
            predicted_qualities = model.predict(test_x)
            # print(predicted_qualities)

            (rsme, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            
            scores = {"rsme":rsme, "mae":mae, "r2":r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            
            
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rsme", rsme)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
                       

            # mlflow.sklearn.log_model(sk_model= model, name="ElasticnetModel")
            # This will log your model as a file without trying to "register" it

            # if tracking_url_type_store != "file":

            #     # Register the model
            #     # There are other ways to use the Model Registry, which depends on the use case,
            #     # please refer to the doc for more information:
            #     # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            #     mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            # else:
            #     mlflow.sklearn.log_model(model, "model")

    
            mlflow.log_artifact(local_path=self.config.model_path, artifact_path="ElasticnetModel")
            # mlflow.sklearn.log_model(sk_model=model)
           
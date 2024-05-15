from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME = "Data evaluation stage"

class DataEvaluationTrainingPipeline:
    def __init__(self):
        None

    def main(self):
        config = ConfigurationManager()
        data_evaluation_config = config.get_model_evaluation_config()
        data_evaluation_config = ModelEvaluation(config = data_evaluation_config)
        data_evaluation_config.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = DataEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
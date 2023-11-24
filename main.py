from textsummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarization.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarization.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textsummarization.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

from textsummarization.logging import logger


STAGE_Name = "Data Ingestion Stage"

try:
    logger.info("********************************************** \n \n")

    logger.info(f">>>>> stage {STAGE_Name} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_Name} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_Name = "Data Validation Stage"

try:
    logger.info("********************************************** \n \n")

    logger.info(f">>>>> stage {STAGE_Name} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_Name} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_Name = "Data Transformation Stage"

try:
    logger.info("********************************************** \n \n")

    logger.info(f">>>>> stage {STAGE_Name} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_Name} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_Name = "Model Trainer Stage"

try:
    logger.info("********************************************** \n \n")
   
    logger.info(f">>>>> stage {STAGE_Name} started <<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_Name} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_Name = "Model Evaluation Stage"

try:
    logger.info("********************************************** \n \n")
    logger.info(f">>>>> stage {STAGE_Name} started <<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_Name} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e
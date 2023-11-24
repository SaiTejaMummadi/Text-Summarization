from textsummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarization.logging import logger


STAGE_Name = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_Name} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_Name} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_Name = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_Name} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_Name} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e
from textsummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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
import os
import datetime

#Pymongo Constants
DB_NAME='ins_motor_db'
COLLECTION_NAME='ins_motor_collection'
MONGODB_URL_KEY='MONGO_INS_URL'


PIPELINE_NAME: str = "ins_motor"
ARTIFACT_DIR: str = "artifact"
MODEL_FILE_NAME = "model.pkl"


TARGET_COLUMN = "ClaimAmount"
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"


FILE_NAME: str = "insmotor.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")



"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "ins_motor_collection"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"



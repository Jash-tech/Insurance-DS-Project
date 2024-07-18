import os
import sys
from insurance_motor_prediction.logger import logging
from insurance_motor_prediction.exception import CustomException
from insurance_motor_prediction.entity.config_entity import DataIngestionConfig
from insurance_motor_prediction.entity.artifact_entity import DataIngestionArtifact
from insurance_motor_prediction.data_access.ins_data import Ins_Data
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from insurance_motor_prediction.data_access.ins_data import Ins_Data


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)

    def export_data_into_feature_store(self):
        try:
            logging.info("Data Ingestion Begins")
            data=Ins_Data()
            
            dataframe = data.export_collection_as_dataframe(collection_name=
                                                                   self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            feature_store_file_path  = self.data_ingestion_config.featured_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
            

        except Exception as e:
            raise CustomException(e,sys)
        
    def split_data_as_train_test(self,dataframe):
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f"Exported train and test file path.")


        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Got the data from mongodb")
            self.split_data_as_train_test(dataframe)

            logging.info("Performed train test split on the dataset")
            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

from insurance_motor_prediction.configuration.mongodb import MongoDBClient
from insurance_motor_prediction.constants import DB_NAME,COLLECTION_NAME
from insurance_motor_prediction.exception import CustomException
import pandas as pd
import sys
from typing import Optional
import numpy as np


class Ins_Data:
    """
    This class help to export entire mongo db record as pandas dataframe
    """
    def __init__(self):
        self.mongodb_client=MongoDBClient(database_name=DB_NAME)

    def export_collection_as_dataframe(self,collection_name,database_name=None):
        try:
            if database_name is None:
                collection = self.mongodb_client.database[collection_name]
            else:
                collection = self.mongodb_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise CustomException(e,sys)





    
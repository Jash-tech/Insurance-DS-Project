import sys

from insurance_motor_prediction.exception import CustomException
from insurance_motor_prediction.logger import logging

import os
from insurance_motor_prediction.constants import DB_NAME, MONGODB_URL_KEY
import pymongo
import certifi


ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient: Conection for MongoDB Database
    
    """
    client=None
    def __init__(self,database_name=DB_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url=os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"{MONGODB_URL_KEY} is not set")
                MongoDBClient.client=pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client=MongoDBClient.client
            self.database=self.client[database_name]
            self.database_name=database_name
            logging.info("MongoDb connection successfull")
        except Exception as e:
            raise CustomException(e,sys)
        

# if __name__=="__main__":
#     obj=MongoDBClient(DB_NAME)
#     print(obj.client)
#     print(obj.database)
#     print(obj.database_name)
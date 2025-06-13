
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass         #used to create special methods like __init__()
class dataingestionconfig:
    train_data_path:str= os.path.join('artifacts',"train.csv")    #path for saving train data
    test_data_path:str= os.path.join('artifacts',"test.csv")      #path for saving test data
    raw_data_path:str= os.path.join('artifacts',"data.csv")

class dataingestion:
    def __init__(self):
        self.ingestion_config = dataingestionconfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")

        try:
            df = pd.read_csv('notebook\\data\\stud.csv')
            logging.info("Read the data set")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #Ensures that the artifacts/ directory exists. If it doesn’t, it creates it.

            df.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)
            #Saves the original dataset as data.csv (raw data) in the artifacts/ directory

            logging.info("Train test split initiated")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            #Saves both the train and test sets into their respective files under the artifacts/ folder

            logging.info("Data ingestion is complete")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path    #Returns the paths to the train and test files 
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = dataingestion()
    obj.initiate_data_ingestion()
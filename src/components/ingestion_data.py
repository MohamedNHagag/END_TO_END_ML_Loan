import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import sys
import os

from src.exception import CustomException
from src.logger import logging

from src.components.transformation_data import datatransformationconfig
from src.components.transformation_data import datatransformation

from src.components.Trainermodel import datatrainer
from src.components.Trainermodel import datatrainerconfig



@dataclass

class dataingestionconfig: #to select paths
    train_data:str=os.path.join("artifical","train.csv")
    test_data:str=os.path.join("artifical","test.csv")
    raw_data:str=os.path.join("artifical","dataset.csv")
    


class dataingestion:
    def __init__(self):#to get object from up class to use 
        self.dataingestionconfig=dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info("goooo to split")

        try:
            #read
            df=pd.read_csv(r'notebook/data/loan_dataset.csv')
            os.makedirs(os.path.dirname(self.dataingestionconfig.train_data),exist_ok=True)
            df.to_csv(self.dataingestionconfig.raw_data,index=False,header=True)
            #split
            train_set,test_set=train_test_split(df,test_size=0.1,random_state=42)
            #save
            train_set.to_csv(self.dataingestionconfig.train_data,index=False,header=True)
            test_set.to_csv(self.dataingestionconfig.test_data,index=False,header=True)

            #return this files
            return(
                self.dataingestionconfig.train_data,
                self.dataingestionconfig.test_data
            )

        except Exception as e:
            raise CustomException(e,sys)
        

#condition for it to work as a group and not be imported into an external Python file        
    
if __name__ == "__main__":
    obj=dataingestion()
    train_data,test_data=obj.initiate_data_ingestion()
    

    data_transform=datatransformation()
    train_arr,test_arr=data_transform.initiate_data_transformation(train_data,test_data)

    model_trainer=datatrainer()
    print(model_trainer.initiate_Model_Trainer(train_arr,test_arr))




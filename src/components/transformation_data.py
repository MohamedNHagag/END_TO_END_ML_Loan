import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,OneHotEncoder,FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer 


import sys
import os 
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.ingestion_data import dataingestion
from src.utilis import save_object

from src.components.Trainermodel import datatrainer
from src.components.Trainermodel import datatrainerconfig




@dataclass

class datatransformationconfig:
    preprocessor_file_path=os.path.join("artifical","preprocessor.pkl")

class transformation:#select path save this obg
    def __init__(self):
        self.transformateconfig=datatransformationconfig()

    #split & steps preprocessor &  apply this preproccing on data and return
    def get_data_transform(self):
        try:#To ensure error handling
            #split data
            numerical_columns=["Gender"	,"Married", "Education"	,"Self_Employed" ,"Property_Area" ,"Loan_Status"]
            category_columns=["Dependents" ,"ApplicantIncome" ,"CoapplicantIncome" ,"LoanAmount"	,"Loan_Amount_Term"	,"Credit_History"]
            
            #handel missing value and standard scaler
            dropna_transformer = FunctionTransformer(lambda x: x.dropna())
            num_pipeline = Pipeline(steps=[
                ("drop_null", dropna_transformer),
                ("scaler", StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])


            #apply this preproccing on data and return
            Preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,category_columns)
            ])
            return Preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        

    #apply on train,test this preproccing after split feature,target
    def initiate_data_transformation(self,train_path,test_path):
        try:
            #read data
            train_df=pd.read_csv(train_path) #train_path==train_data is coming from ingestion
            test_df=pd.read_csv(test_path)
            #get obg preprocing 
            preproccing_obg=self.get_data_transform()
            #seprate target becouse dont show
            target="Loan_Status"
            #seprate target becouse dont show
            input_train=train_df.drop(columns="Loan_Status",axis=1)
            target_train=train_df["Loan_Status"]
            input_test=test_df.drop(columns="Loan_Status",axis=1)
            target_test=test_df["Loan_Status"]

            #apply obj preproccing
            input_train_arr=preproccing_obg.fit_transform(input_train)
            input_test_arr=preproccing_obg.transform(input_test)

            #++++ features after preproccing + target
            train_arr=np.c_[input_train_arr,np.array(target_train)]
            test_arr=np.c_[input_test_arr,np.array(target_test)]

            #save
            save_object(
                file_path=self.transformateconfig.preprocessor_file_path,
                obj=preproccing_obg
            )

            #return data after cleaning 
            return(train_arr,test_arr,self.transformateconfig.preprocessor_file_path)






        except Exception as e:
            raise CustomException(e,sys)

import os 
import sys

import pandas as pd

from src.exception import CustomException
from src.utilis import save_object


class predictionpipeline:#✅ prepare data and predict
    def __init__(self):
        pass
    def predict(self,feature):
        try:
            #get path objects
            Model_path=os.path.join("artifical","Modelloan.pkl")
            preprocessing_path=os.path.join("artifical","preprocessor.pkl")

            #load
            model=load_object(file_path=Model_path)
            preprocessing=load_object(file_path=preprocessing_path)
            #work preproccing and predict
            data_scaled=preprocessing.transform(feature)
            predicts=model.predict(data_scaled)

            return predicts
        except Exception as e:
            raise CustomException(e,sys)
        


#✅ specific inputs
class custmerdata:
    #specific inputs feature
    def __init__(  self,
        Gender: str,
        Married: str,
        Dependents:int,
        Education: str,
        Self_Employed: str,
        ApplicantIncome: int,
        CoapplicantIncome: int,
        LoanAmount: int,
        Loan_Amount_Term: int,
        Credit_History: int,
        Property_Area: str
        
        ):

        #تقوم بتعيين هذه المدخلات كخصائص 
        self.Gender = Gender
        self.Married = Married
        self.Dependents = Dependents
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.ApplicantIncome = ApplicantIncome
        self.CoapplicantIncome = CoapplicantIncome
        self.LoanAmount = LoanAmount
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.Property_Area = Property_Area


        #create Dictianary and convert to data frame
        def get_data_to_dataframe(self):
            try:
                custmerdata_dic={
                    "Gender": [self.Gender],
                    "Married": [self.Married],
                    "Dependents":[self.Dependents],
                    "Education": [self.Education],
                    "Self_Employed":[ self.Self_Employed],
                    "ApplicantIncome":[ self.ApplicantIncome],
                    "CoapplicantIncome":[ self.CoapplicantIncome],
                    "LoanAmount": [self.Loan_Amount_Term],
                    "Loan_Amount_Term":[ self.Loan_Amount_Term],
                    "Credit_History": [self.Credit_History],
                    "Property_Area": [self.Property_Area] }
                    return pd.DataFrame(custmerdata_dic)

            except Exception as e:
                raise CustomException(e,sys)




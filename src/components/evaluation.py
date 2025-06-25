import sys
import os
import pandas as pd
import numpy as np


from sklearn.model_selection import RandomizedSearchCV,GridSearchCV
from sklearn.metrics import accuracy_score,f1_score,classification_report

from src.logger import logging
from src.exception import CustomException



def evaluate_model(x_train,y_train,x_test,y_test,params:dict,models:dict):
    try:
        model_report={}
        for name,obj_model in models.items():
            #if find hyparameter in model
            if name in params and params[name]:
                #get best parameter
                Randomsearch=RandomizedSearchCV(
                            estimator=obj_model,
                            params_cook=params[name],
                            n_iter=10,
                            cv=5,
                            verbose=0,
                            random_state=42,
                            n_jobs=-1
                )
                #train on model have best parameter
                Randomsearch.fit(x_train,y_train)
                best_model=Randomsearch.best_estimator_

            #not found hyparameter in model
            else:
                #train Along
                best_model=obj_model
                best_model.fit(x_train,y_train)
            #predict
            predict=best_model.predict(x_test)
            #accuracy
            accuracy=accuracy_score(y_test,predict)
            f1=f1_score(y_test,predict)
            report=classification_report(y_test,predict)
            #collect best model,accuracy
            model_report[name]={
                "BestModel":best_model,
                "accuarcy":accuracy,
                "f-1":f1,
                "report":report
            }
            return model_report



    except Exception as e:
        raise CustomException(e,sys)


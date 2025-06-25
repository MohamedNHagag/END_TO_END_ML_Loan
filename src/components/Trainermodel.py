import os
import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np 

from sklearn.metrics import f1_score,accuracy_score,classification_report,confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC

from src.logger import logging
from src.exception import CustomException
from src.utilis import save_object 
from src.components.evaluation import evaluate_model





@dataclass

class modeltrainconfig:#select path model trainer
    trainModel_path=os.path.join("artifical","Modelloan.pkl")


class modeltrain:
    def __init__(self):
        self.modeltrainconfig=modeltrainconfig()

    def initiate_model_train(self,train_array,test_array):
        try:
            #split to train,test
            x_train,x_test,y_train,y_test=(train_array[:,:-1],
                                            train_array[:,-1],
                                            test_array[:,:-1],
                                            test_array[:,-1]
                                            )
            #Define and take an object
            models={
                    "LogisticRegression":LogisticRegression(),
                    "tree":DecisionTreeClassifier(),
                    "knn":KNeighborsClassifier(),
                    "svc":SVC(),
                    "XGBClassifier":XGBClassifier(),
                    "CatBoostClassifier":CatBoostClassifier(),
                    "RandomForest":RandomForestClassifier(),
                    "AdaBoost":AdaBoostClassifier()
            }
            #Define Hyparameter
            params={
                    "LogisticRegression": {
                        'C': [0.01, 0.1, 1, 10],
                        'solver': ['liblinear', 'lbfgs']
                    },
                    "tree": {
                        'criterion': ['gini', 'entropy'],
                        'max_depth': [3, 5, 10, None],
                        'splitter': ['best', 'random']
                    },
                    "RandomForest": {
                        'n_estimators': [50, 100, 200],
                        'max_features': ['sqrt', 'log2'],
                        'criterion': ['gini', 'entropy']
                    },
                    "knn": {
                        'n_neighbors': [3, 5, 7, 9],
                        'weights': ['uniform', 'distance'],
                        'metric': ['euclidean', 'manhattan']
                    },
                    "SVC": {
                        'C': [0.1, 1, 10],
                        'kernel': ['linear', 'rbf', 'poly'],
                        'gamma': ['scale', 'auto']
                    },
                    "AdaBoost": {
                        'n_estimators': [50, 100, 200],
                        'learning_rate': [0.01, 0.1, 1]
                    },
                    "GradientBoost": {
                        'n_estimators': [50, 100, 150],
                        'learning_rate': [0.01, 0.1, 0.2],
                        'subsample': [0.8, 1.0]
                    },
                    "XGBoost": {
                        'n_estimators': [50, 100, 200],
                        'learning_rate': [0.01, 0.1, 0.2],
                        'max_depth': [3, 5, 7]
                    },
                    "CatBoost": {
                        'iterations': [50, 100],
                        'depth': [4, 6, 8],
                        'learning_rate': [0.01, 0.1]
                    }
                    }

                #evaluate
                model_report = evaluate_model(x_train, y_train, x_test, y_test, models)

                #get best model
                best_model=max(model_report.values())
                best_model_name = [k for k, v in model_report.items() if v == best_model][0]
                best_model = models[best_model_name]
                best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model)]

                #condation accuracy <0.6 say not found model
                if best_model < 0.6:
                        raise CustomException("not found Best Model")
                    logging.info("not find best model")
            

                #save
                save_object(
                    file_path=self.modeltrainconfig.trainModel_path,
                    obj=best_model
                )

                #جرب
                predict=best_model.predict(x_test)
                accuracy=accuracy_score(y_test,predict)
                return accuracy





        except Exception as e:
            raise CustomException()

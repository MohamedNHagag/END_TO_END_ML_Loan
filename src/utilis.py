
#أدوات مساعدة تستخدمها في أي جزء من المشروع.
#بيحتوي على دوال عامة بتتعامل مع:
#حفظ وتحميل الملفات (مثل النماذج).
#تقييم النماذج.
#إدارة الأخطاء.

#الفكره العامه 
#save_object	لحفظ أي كائن (Model, Preprocessor, ...) كملف .pkl لاستخدامه لاحقا 
#load_object    لتحميل ملف Pickle محفوظ سابقًا
#evaluate_models  تجربة النماذج المتعددة + اختيار أفضل Hyperparameters










import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException





def save_object(file_path, obj): #save object to use later
    try:#to handel mistakes
        #Extraction father from total path ex)artifical/model.pkl->artifical /and check if not found(artifical)
        dir_path = os.path.dirname(file_path) 
        os.makedirs(dir_path, exist_ok=True)
        #open file and save 
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)


    except Exception as e:
        raise CustomException(e, sys)
    






def load_object(file_path):#load object Pre-saved in this path
    try:
        #open file and load
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj) 

    except Exception as e:
        raise CustomException(e, sys)
    












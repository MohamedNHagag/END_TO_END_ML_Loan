import sys
from src.logger import logging

#style error
def error_message_details(error,error_details:sys):
    _,_,exc_tb=error.exc_info() #تجيب التراك 
    file_name=exc_tb.tb_frame.f_code.co_filename # وتجيب الاسكربت الي مكتوب في الخطا
    error_message="the error find in script name[{0}] line number[{1}] message error[{2}]".format(file_name,exc_tb.tb_lineno,str(error)) #شكل الرساله الي هتظهر
    return error_message #رجعلنا الرساله 
    




class CustomException(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message) #خد الورث من customexception الي هي error_message
        self.error_message=error_message_detail(error_message,error_details=error_details) #تبني رساله غنيه بالمعلومات تحتوي علي error_message الي عملتها , error_details من sys

    def __str__(self):#لتحويل الكائن لنص 
        return self.error_message






















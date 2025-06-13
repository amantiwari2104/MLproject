
import sys
from src.logger import logging

def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #sys.exc_info() returns a tuple: (exception_type, exception_value, traceback_object)
                                         #we only need traceback object so other two are just stored
    file_name = exc_tb.tb_frame.f_code.co_filename 
                                         #tb_frame gives the frame object,f_code gives the code object and
                                         #co_filename gives the filename of the script where the error happened
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error) 
                                         #It creates a descriptive error message 
    )
    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
                    #Overrides the __str__ method so when you print the exception, you get the full, detailed error message.
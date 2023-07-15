import sys
import logging
from datetime import datetime
from enum import Enum
from sqlalchemy.exc import StatementError
 
def convert_text_to_date(text):
    try:
        if len(text) > 2:
            return datetime.strptime(text, '%d/%m/%Y')
        return None
    except ValueError as e:
        print('invalid date format')
        raise e

class Result:
    def __init__(self, status, contents, message = None):
        self.status = status
        self.contents = contents
        self.message = message

def service_handler(fnc):
    def handler(*args, **kwargs):
        try:
            return Result(True, fnc(*args, **kwargs))
        except:
            logging.warning(sys.exc_info())
            return Result(False, None)
    return handler
    
    
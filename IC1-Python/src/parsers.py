from datetime import datetime
from typing import *

def parse_boolean(cadena:str)->bool:
    result = False
    if cadena.upper() == 'TRUE':
        result = True
    return result

def parse_datetime(cadena:str, formato:str)->datetime:
    return datetime.strptime(cadena, formato)
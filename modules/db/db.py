from utils import functions as _functions
from mongoengine import *

def instance():
    connect (
                _functions.Config['db']['name'],
                host=_functions.Config['db']['host'],
                port=_functions.Config['db']['port']
            )

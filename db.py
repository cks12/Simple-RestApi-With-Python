from time import sleep
from uuid import uuid4
import pandas as pd

class Users_db:
    def __init__(self):
        self._db_Loc_ = 'db/users.csv'
        self._data_ = pd.read_csv(self._db_Loc_)
    
    def get_database (self):
        return self._data_.to_dict()
    
    def set_newUserInDataBase(self, obj:dict):
        obj["userId"] = str(uuid4())
        obj["locations"] = obj["locations"] if obj["locations"] else []
        new_data = pd.DataFrame([obj])
        self._data_ = pd.concat([new_data,self._data_])
        self._data_.to_csv(self._db_Loc_, index=False)
        return obj
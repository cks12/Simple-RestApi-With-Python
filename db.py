import ast
from uuid import uuid4
import pandas as pd
import pathlib
import os

class Users_db:
    def __init__(self):
        self._userModal_ = {
            "name":str,
            "city":str,
            "locations":[],
            "userId":str,
        }
        self._db_Loc_ = 'db/users.csv'
        self.__createDatabse__()
        self._data_ = pd.read_csv(self._db_Loc_)
    
    def get_database (self):
        list = self._data_.values.tolist()
        listOfElement = []
        for element in list:
            el={}
            for index, key in enumerate(self._userModal_):
                el[key] = element[index]
            listOfElement.append(el)
        return listOfElement

    def create_database(self):
        keys = []
        for key in self._userModal_:
            keys.append(key)
        newTable = pd.DataFrame(columns=[keys])
        file = pathlib.Path(self._db_Loc_)
        file.touch(exist_ok=True)
        newTable.to_csv(self._db_Loc_, index=False)
        print(str(newTable))
        
    
    def __createDatabse__(self):
        exist = os.path.exists(self._db_Loc_)
        if not exist:
            self.create_database()

    def set_newUserInDataBase(self, obj:dict):
        obj["userId"] = str(uuid4())
        obj["locations"] = obj["locations"] if obj["locations"] else []
        new_data = pd.DataFrame([obj])
        self._data_ = pd.concat([new_data,self._data_])
        self._data_.to_csv(self._db_Loc_, index=False)
        return obj
    
    def update_User(self, obj:dict):
        try:
            user = self._data_.find(obj["userId"])
        except:
            return {
                "err": "{} user not found".format(obj["userId"])
            }
        
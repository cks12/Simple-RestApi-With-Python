import ast
from uuid import uuid4
import pandas as pd
import os

class Users_db:
    def __init__(self):
        self._db_Loc_ = 'db/users.csv'
        self._data_ = pd.read_csv(self._db_Loc_)
        self._userModal_ = {
            name:str,
            userId:str,
            city:str,
            locations:[],

        }
        
    
    def get_database (self):
        return self._data_.to_dict()

    def create_database(self):
        keys = []
        for index in self._userModal_:
            keys.append(index)

        newTable = pd.DataFrame(columns=keys)
    
    def __createDatabse__(self):
        pass;

    def set_newUserInDataBase(self, obj:dict):
        obj["userId"] = str(uuid4())
        obj["locations"] = obj["locations"] if obj["locations"] else []
        new_data = pd.DataFrame([obj])
        self._data_ = pd.concat([new_data,self._data_])
        self._data_.to_csv(self._db_Loc_, index=False)
        return obj
    
    def update_User(self, obj:dict):
        try:
            data = self.get_database()
            userData = data[data["userId"] == obj["userId"]]
            userData["locations"] = userData["locations"].values[0].append(obj["location"])
            self._data_.to_csv(self._db_Loc_, index=False)
            return {data} 
        except:
            return {
                "err": "{} user not found".format(obj["userId"])
            }
        
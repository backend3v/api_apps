from domain.i_user import IUser
import re

class User(IUser):
    def __init__(self, kwargs):
        super().__init__(**kwargs)
    def create(self):
        return self
    
    def get(self):
        return {k.replace("_","",1):v for k,v in self.__dict__.items() if k != "password"}
    
    def get_update(self):
        list_update_fields = ['name', 'phone', 'job_place']
        return {k.replace("_","",1):v for k,v in self.__dict__.items() if k in list_update_fields}
    def modify(self):

        return self.__dict__
    
    def delete(self):
        return self.__dict__
    
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def set_object(self, data):
        for k, v in data.items():
            self.__setattr__(k, v)
        return self
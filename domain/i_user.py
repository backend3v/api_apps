from abc import ABC, abstractmethod

class IUser(ABC):
    def __init__(self, name :str=None, email :str=None,password :str=None,phone :str=None,job_place :str=None):
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to None.
            email (str, optional): _description_. Defaults to None.
            password (str, optional): _description_. Defaults to None.
            phone (str, optional): _description_. Defaults to None.
            job_place (str, optional): _description_. Defaults to None.
        """        
        self.name :str = name
        self.email :str = email
        self.password :str = password
        self.phone :str = phone
        self.job_place :str = job_place

    @abstractmethod
    def create(self):
        pass
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def modify(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    

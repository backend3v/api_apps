from abc import ABC, abstractmethod

class IResource(ABC):
    def __init__(self, name :str=None, type :str=None,theme :str=None,content :str=None):     
        self.name :str = name
        self.type :str = type
        self.theme :str = theme
        self.content :dict = content

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

    

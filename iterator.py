from abc import ABC, abstractmethod

class Iterator(ABC):

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
   

class Iterable(ABC):

    @abstractmethod
    def __iter__(self):
        pass


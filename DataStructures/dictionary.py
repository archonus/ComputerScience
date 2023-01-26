from abc import ABC, abstractmethod

class Dictionary(ABC):
    @abstractmethod
    def retrieve(self, key):
        pass

    @abstractmethod
    def insert(self, key, value):
        pass

    @abstractmethod
    def update(self, key, value):
        pass

    def __getitem__(self, key):
        return self.retrieve(key)

    def __setitem__(self, key, value):
        try:
            self.update(key, value)
        except KeyError:  # If the item does not exist, insert it
            self.insert(key, value)
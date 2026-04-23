from abc import ABC, abstractmethod

class LivroRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass
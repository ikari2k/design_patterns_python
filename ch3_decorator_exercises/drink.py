from abc import abstractmethod, ABC

class Drink(ABC):

    def __init__(self):
        self.description = "Unknown drink"

    def get_description(self):
        return self.description

    @abstractmethod
    def get_price(self):
        pass
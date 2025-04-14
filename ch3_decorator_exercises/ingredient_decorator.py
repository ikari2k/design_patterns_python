from abc import abstractmethod

from ch3_decorator_exercises.drink import Drink


class Ingredient (Drink):

    @abstractmethod
    def get_description(self):
        pass
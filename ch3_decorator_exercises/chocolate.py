from ch3_decorator_exercises.ingredient_decorator import Ingredient


class Chocolate(Ingredient):
    def __init__(self, drink):
        self.drink = drink
        self.description = "Chocolate"

    def get_price(self):
        return self.drink.get_price() + 1.1

    def get_description(self):
        return self.drink.get_description() + ", chocolate"

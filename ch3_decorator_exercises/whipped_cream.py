from ch3_decorator_exercises.ingredient_decorator import Ingredient


class WhippedCream(Ingredient):
    def __init__(self, drink):
        self.drink = drink
        self.description = "Whipped Cream"

    def get_price(self) -> float:
        return self.drink.get_price() + 0.69

    def get_description(self):
        return self.drink.get_description() + ", whipped cream"

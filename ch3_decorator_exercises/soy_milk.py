from ch3_decorator_exercises.ingredient_decorator import Ingredient


class SoyMilk(Ingredient):
    def __init__(self, drink):
        super().__init__()
        self.drink = drink
        self.description = "Soy Milk"

    def get_price(self):
        return self.drink.get_price() + 0.55

    def get_description(self):
        return self.drink.get_description() + ", soy milk"

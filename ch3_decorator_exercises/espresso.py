from ch3_decorator_exercises.drink import Drink


class Espresso(Drink):

    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def get_price(self):
        return 6.49

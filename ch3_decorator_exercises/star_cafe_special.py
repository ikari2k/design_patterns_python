from ch3_decorator_exercises.drink import Drink


class StarCafeSpecial(Drink):

    def __init__(self):
        super().__init__()
        self.description = "Star Cafe Special"

    def get_price(self):
        return 4.99

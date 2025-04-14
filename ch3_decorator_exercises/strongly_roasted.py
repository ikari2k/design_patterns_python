from ch3_decorator_exercises.drink import Drink


class StronglyRoasted(Drink):

    def __init__(self):
        super().__init__()
        self.description = "Strongly Roasted Coffee"

    def get_price(self):
        return 5.21

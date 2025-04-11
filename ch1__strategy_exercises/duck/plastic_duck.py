from duck import Duck
from fly_behavior import NoFly
from quack_behavior import Silent


class PlasticDuck(Duck):
    def __init__(self):
        super().__init__(NoFly(), Silent())

    def display(self):
        print("I'm a plastic duck.")

from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior


class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    def display(self):
        print("I'm a duck!")

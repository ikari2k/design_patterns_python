from abc import ABC, abstractmethod


# Fly behavior
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with wings!")


class NoFly(FlyBehavior):
    def fly(self):
        print("I can't fly.")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("Flying with a rocket!")

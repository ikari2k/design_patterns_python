from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack!")


class Silent(QuackBehavior):
    def quack(self):
        print("...")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak!")

class LoadMusic(QuackBehavior):
    def quack(self):
        print("Loading music...")
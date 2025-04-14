from abc import ABC, abstractmethod

from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class Pizzeria(ABC):

    def order_pizza(self, kind: str) -> Pizza:
        pizza: Pizza = self.create_pizza(kind)
        if pizza is None:
            raise ValueError(f"Pizza type '{kind}' is not recognized.")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        pass

from ch4_factory_exercises.pizza_factory_1.italian_veggie_pizza import ItalianVeggiePizza
from ch4_factory_exercises.pizza_factory_1.italian_cheese_pizza import ItalianCheesePizza
from ch4_factory_exercises.pizza_factory_1.italian_clam_pizza import ItalianClamPizza
from ch4_factory_exercises.pizza_factory_1.italian_pepperoni_pizza import ItalianPepperoniPizza
from ch4_factory_exercises.pizza_factory_1.pizza import Pizza
from ch4_factory_exercises.pizza_factory_1.pizzeria import Pizzeria


class ItalianPizzeria(Pizzeria):

    def __init__(self):
        super().__init__()
        self.name = "Italian Pizzeria"


    def create_pizza(self, kind) -> Pizza | None:
        if kind == "cheese":
            return ItalianCheesePizza()
        elif kind == "pepperoni":
            return ItalianPepperoniPizza()
        elif kind == "clam":
            return ItalianClamPizza()
        elif kind == "veggie":
            return ItalianVeggiePizza()
        else:
            return None
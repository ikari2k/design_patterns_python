from ch4_factory_exercises.pizza_factory_1.american_cheese_pizza import AmericanCheesePizza
from ch4_factory_exercises.pizza_factory_1.american_clam_pizza import AmericanClamPizza
from ch4_factory_exercises.pizza_factory_1.american_pepperoni_pizza import AmericanPepperoniPizza
from ch4_factory_exercises.pizza_factory_1.american_veggie_pizza import AmericanVeggiePizza
from ch4_factory_exercises.pizza_factory_1.pizza import Pizza
from ch4_factory_exercises.pizza_factory_1.pizzeria import Pizzeria


class AmericanPizzeria(Pizzeria):

    def __init__(self):
        super().__init__()
        self.name = "American Pizzeria"

    def create_pizza(self, kind) -> Pizza | None:
        if kind == "cheese":
            return AmericanCheesePizza()
        elif kind == "pepperoni":
            return AmericanPepperoniPizza()
        elif kind == "veggie":
            return AmericanVeggiePizza()
        elif kind == "clam":
            return AmericanClamPizza()
        else:
            return None

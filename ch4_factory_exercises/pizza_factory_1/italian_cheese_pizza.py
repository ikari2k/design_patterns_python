from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class ItalianCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Italian Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings.append("Reggiano Cheese")
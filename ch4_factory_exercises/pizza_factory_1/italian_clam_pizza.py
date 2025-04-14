from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class ItalianClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Italian Clam Pizza"
        self.dough = "Thin Crust"
        self.sauce = "Marinara Sauce"

        self.toppings.append("Fresh Clams from Long Island Sound")
        self.toppings.append("Oregano Cheese")


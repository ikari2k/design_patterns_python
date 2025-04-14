from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class AmericanClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Clam Pizza"
        self.dough = "Thin Crust"
        self.sauce = "White Garlic Sauce"

        self.toppings.append("Fresh Clams from Long Island Sound")
        self.toppings.append("Sliced Pepperoni")

    def cut(self):
        print("Cutting the pizza into square slices")
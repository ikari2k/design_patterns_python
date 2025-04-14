from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class AmericanPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Black Olives")
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Grated parmesan cheese")
        self.toppings.append("Sliced Mushrooms")

    def cut(self):
        print("Cutting the pizza into square slices")

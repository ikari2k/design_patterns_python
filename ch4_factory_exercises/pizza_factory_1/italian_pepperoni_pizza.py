from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class ItalianPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Italian Pepperoni Pizza"
        self.dough = "Light Crust"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Black Olives")
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Sliced Onion")
        self.toppings.append("Grated parmesan cheese")
        self.toppings.append("Sliced Mushrooms")

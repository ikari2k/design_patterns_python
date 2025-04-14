from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class AmericanCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "American Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")
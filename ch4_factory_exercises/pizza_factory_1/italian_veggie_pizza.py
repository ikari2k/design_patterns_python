from ch4_factory_exercises.pizza_factory_1.pizza import Pizza


class ItalianVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Italian Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")

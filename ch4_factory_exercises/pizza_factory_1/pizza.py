from abc import ABC


class Pizza(ABC):
    def __init__(self):
        self.name: str = ""
        self.dough: str = ""
        self.sauce: str = ""
        self.toppings: list[str] = []


    def get_name(self):
        return self.__str__()

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Making dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(f" {topping}")

    def bake(self) -> None:
        print(f"Baking 25 minutes in 180 degree Celsius")

    def cut(self):
        print(f"Cutting pizza in 8 slices")

    def box(self):
        print(f"Boxing pizza")

    def __str__(self):
        display: str = ""
        display += "\n---- " + self.name + " ----\n"
        display += self.dough + "\n"
        display += self.sauce + "\n"
        for topping in self.toppings:
            display += topping + "\n"
        return display

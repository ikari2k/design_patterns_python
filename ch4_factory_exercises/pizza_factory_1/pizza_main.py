from ch4_factory_exercises.pizza_factory_1.american_pizzeria import AmericanPizzeria
from ch4_factory_exercises.pizza_factory_1.italian_pizzeria import ItalianPizzeria
from ch4_factory_exercises.pizza_factory_1.pizza import Pizza
from ch4_factory_exercises.pizza_factory_1.pizzeria import Pizzeria


italian: Pizzeria = ItalianPizzeria()
american: Pizzeria = AmericanPizzeria()

pizza: Pizza = italian.order_pizza("cheese")
print(f"Order received: {pizza.get_name()}")

pizza: Pizza = american.order_pizza("cheese")
print(f"Order received: {pizza.get_name()}")

pizza: Pizza = italian.order_pizza("pepperoni")
print(f"Order received: {pizza.get_name()}")

pizza: Pizza = american.order_pizza("pepperoni")
print(f"Order received: {pizza.get_name()}")

pizza: Pizza = italian.order_pizza("clam")
print(f"Order received: {pizza.get_name()}")

pizza: Pizza = american.order_pizza("clam")
print(f"Order received: {pizza.get_name()}")

pizza: Pizza = italian.order_pizza("veggie")
print(f"Order received: {pizza.get_name()}")

pizza: Pizza = american.order_pizza("veggie")
print(f"Order received: {pizza.get_name()}")


from ch3_decorator_exercises.chocolate import Chocolate
from ch3_decorator_exercises.drink import Drink
from ch3_decorator_exercises.espresso import Espresso
from ch3_decorator_exercises.soy_milk import SoyMilk
from ch3_decorator_exercises.star_cafe_special import StarCafeSpecial
from ch3_decorator_exercises.strongly_roasted import StronglyRoasted
from ch3_decorator_exercises.whipped_cream import WhippedCream

drink: Drink = Espresso()
print(f"{drink.get_description()} ${drink.get_price()}")

drink2: Drink = StronglyRoasted()
drink2 = Chocolate(drink2)
drink2 = Chocolate(drink2)
drink2 = WhippedCream(drink2)
print(f"{drink2.get_description()} ${drink2.get_price()}")

drink3:  Drink = StarCafeSpecial()
drink3 = Chocolate(drink3)
drink3 = WhippedCream(drink3)
drink3 = SoyMilk(drink3)
print(f"{drink3.get_description()} ${drink3.get_price()}")

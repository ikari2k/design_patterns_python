from mallard_duck import MallardDuck
from plastic_duck import PlasticDuck
from quack_behavior import LoadMusic
from fly_behavior import FlyRocketPowered

def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_fly()
    mallard.perform_quack()

    print()

    plastic = PlasticDuck()
    plastic.display()
    plastic.perform_fly()
    plastic.perform_quack()

    # Change behavior on the fly
    print("\nUpgrading plastic duck to have a speaker and wings!")
    plastic.set_quack_behavior(LoadMusic())
    plastic.set_fly_behavior(FlyRocketPowered())
    plastic.perform_fly()
    plastic.perform_quack()


if __name__ == "__main__":
    main()

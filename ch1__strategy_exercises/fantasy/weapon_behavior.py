from abc import ABC, abstractmethod


class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        pass


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Swinging a sword!")


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Shooting an arrow with a bow!")


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Chopping with an axe!")


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Stabbing with a knife!")

from weapon_behavior import WeaponBehavior


class Character:
    def __init__(self, weapon_behavior: WeaponBehavior):
        self.weapon_behavior = weapon_behavior

    def fight(self):
        self.weapon_behavior.use_weapon()

    def set_weapon_behavior(self, weapon_behavior):
        self.weapon_behavior = weapon_behavior

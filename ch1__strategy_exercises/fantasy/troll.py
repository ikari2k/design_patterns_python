from character import Character
from weapon_behavior import AxeBehavior


class Troll(Character):
    def __init__(self):
        super().__init__(AxeBehavior())

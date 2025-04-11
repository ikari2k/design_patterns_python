from character import Character
from weapon_behavior import KnifeBehavior


class Knight(Character):
    def __init__(self):
        super().__init__(KnifeBehavior())

from character import Character
from weapon_behavior import BowAndArrowBehavior


class Queen(Character):
    def __init__(self):
        super().__init__(BowAndArrowBehavior())

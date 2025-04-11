from character import Character
from weapon_behavior import SwordBehavior


class King(Character):
    def __init__(self):
        super().__init__(SwordBehavior())

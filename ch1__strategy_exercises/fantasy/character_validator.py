from king import King
from knight import Knight
from queen import Queen
from troll import Troll
from weapon_behavior import KnifeBehavior


def main():
    king = King()
    king.fight()

    queen = Queen()
    queen.fight()
    queen.set_weapon_behavior(KnifeBehavior())
    queen.fight()

    troll = Troll()
    troll.fight()

    knight = Knight()
    knight.fight()


if __name__ == "__main__":
    main()

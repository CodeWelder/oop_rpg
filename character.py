"""Character class module."""
from dataclasses import dataclass
from typing import ClassVar

from race import Race, Human
from classes import CharClass, NoClass


@dataclass
class Character():
    """
    The class for creating all creatures and race in the game.
    Arguments: personal name, Race object, CharClass object
    and boolean is it player or not.
    All arguments are optional.
    """
    # Base stats for all creatures and race
    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 10,
        'AGI': 10,
        'CON': 10,
        'INT': 10,
        }

    name: str = ''
    race_: Race = Human
    class_: CharClass = NoClass
    is_player: bool = False

    # Actions from this set will be available
    # to all creatures
    actions: ClassVar[set[str]] = {
        'attack',
        'defence',
    }

    def get_stats(self) -> dict[str, int]:
        """
        Returns dict with actual stats of a character,
        which is sum of BASE_STATS from:
        Character (this class), Race and CharClass.
        """
        stats: dict[str, int] = dict()
        for key in self.BASE_STATS:
            stats[key] = (self.BASE_STATS[key]
                          + self.race_.BASE_STATS[key]
                          + self.class_.BASE_STATS[key]
                          )
        return stats

    def update_actions(self) -> None:
        self.actions.update(self.race_.actions)
        self.actions.update(self.class_.actions)

    def __post_init__(self) -> None:
        self.update_actions()


# for testing purpose
if __name__ == '__main__':
    from race import all_race
    from classes import all_classes

    bob = Character('Bob', all_race['rat'], all_classes['warrior'])
    print(bob)
    print(bob.get_stats())
    print(bob.actions)

"""Character class module."""
from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from actions import Action


@dataclass
class CharacterAttribute():
    """Base class for race and classes."""
    NAME: ClassVar[str] = ''
    IS_PLAYABLE: ClassVar[bool] = False
    DESCRIPTION: ClassVar[str] = ''

    # the stats will increase character' base stats
    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0,
        'AGI': 0,
        'CON': 0,
        'INT': 0,
        }

    # posible actions
    actions: ClassVar[set[type[Action]]] = set()

    def __str__(self) -> str:
        return (f'{self.NAME} - {self.DESCRIPTION}.').capitalize()

    @classmethod
    def describe(cls) -> str:
        return (f'{cls.NAME} - {cls.DESCRIPTION}.').capitalize()


@dataclass
class Character():
    """
    Arguments: personal name, Race class, CharClass class
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

    # used to count characteristics derived from basic stats
    BASE_STATS_MULTIPLIER: ClassVar[int] = 10

    name: str
    race_: type[CharacterAttribute]
    class_: type[CharacterAttribute]
    is_player: bool = False

    # characteristics derived from basic stats
    health: int = 0
    stamina: int = 0
    mana: int = 0

    # Actions from this set will be available
    # to all creatures
    actions: ClassVar[set[type[Action]]] = set()
    # = {
    #     act.Attack,
    #     act.Defence,
    # }

    def get_all_stats(self) -> dict[str, int]:
        """
        Returns dict with all actual stats of a character,
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

    def get_stats(self, stat_name: str) -> int:
        """Returns int with actual value of one of BASE_STATS."""
        result: int = (self.BASE_STATS[stat_name]
                       + self.race_.BASE_STATS[stat_name]
                       + self.class_.BASE_STATS[stat_name])
        return result

    def update_actions(self) -> None:
        self.actions.update(self.race_.actions)
        self.actions.update(self.class_.actions)

    # get short description of a character
    # i.e. "Bob the Goblin Warrior"
    def __str__(self) -> str:
        return (f'{self.name} '
                f'the {self.race_.NAME.capitalize()} '
                f'{self.class_.NAME.capitalize()}')

    # get long descriprions with stats and characteristics
    def __repr__(self) -> str:
        return (f'{str(self)}.\n'
                f'Stats: {self.get_all_stats()}')

    def __post_init__(self) -> None:
        self.update_actions()
        # update characteristics
        self.health = self.BASE_STATS_MULTIPLIER * self.get_stats('CON')
        self.stamina = self.BASE_STATS_MULTIPLIER * self.get_stats('AGI')
        self.mana = self.BASE_STATS_MULTIPLIER * self.get_stats('INT')


# for testing purpose
if __name__ == '__main__':
    from races import all_race
    from classes import all_classes

    bob = Character('Bob', all_race['rat'], all_classes['warrior'])
    print(str(bob.actions))

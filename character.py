"""Character class module."""
from __future__ import annotations
from dataclasses import dataclass, field
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
        'STR': 0, 'AGI': 0, 'CON': 0, 'INT': 0,
        }

    # posible actions
    actions: ClassVar[set[type[Action]]] = set()

    def __str__(self) -> str:
        return (f'{self.NAME} - {self.DESCRIPTION}.').capitalize()

    def __post_init__(self) -> None:
        # all parent classes
        # except instance's class and class 'object'
        parents = type(self).__mro__[1:-1]
        for parent in parents:
            try:
                self.actions.update(parent.actions)
            except AttributeError:
                pass


@dataclass
class Character():
    """
    Arguments: personal name, Race class, CharClass class
    and boolean is it player or not.
    All arguments are optional.
    """
    # Base stats for all creatures and race
    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 10, 'AGI': 10, 'CON': 10, 'INT': 10,
        }

    # used to count characteristics derived from basic stats
    BASE_STATS_MULTIPLIER: ClassVar[int] = 10

    name: str
    race_: CharacterAttribute
    class_: CharacterAttribute
    is_player: bool = False

    # characteristics derived from basic stats
    health: int = 0
    stamina: int = 0
    mana: int = 0

    # Actions from this set will be available
    # to all creatures
    actions: set[type[Action]] = field(default_factory=set)

    def get_stat_bar(
        self,
        stat: str = 'HP',
        left_side: bool = True,
    ) -> str:
        """Returns bar of HP (health), SP (stamina) or MP (mana)."""
        BAR_RESOLUTION: int = 5

        stat_value_mapping: dict[str, int] = {
            'HP': self.health,
            'SP': self.stamina,
            'MP': self.mana,
        }
        stat_symbol_mapping: dict[str, str] = {
            'HP': '█',
            'SP': '░',
            'MP': '▓',
        }

        stat_value: int = stat_value_mapping[stat]
        stat_symbol: str = stat_symbol_mapping[stat]
        bar: str = int(stat_value / BAR_RESOLUTION) * stat_symbol
        result: str = ''

        if left_side is True:
            result: str = f'{stat} {bar} {stat_value}'
        else:
            result: str = f'{stat_value} {bar} {stat}'

        return result

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
        self.actions.clear()
        self.actions.update(self.race_.actions)
        self.actions.update(self.class_.actions)

    def get_actions_list(self) -> list[type[Action]]:
        return sorted(list(self.actions), key=(lambda x: x.NAME))

    def perform_action(
            self,
            action: type[Action],
            target: Character = None
    ) -> tuple[int, int]:
        performed_action = action(self, target)
        performed_action.describe_action()
        return performed_action.execute()

    def __str__(self) -> str:
        """
        Return short description of a character\n
        i.e. 'Bob the Goblin Warrior'.
        """
        return (f'{self.name} '
                f'the {self.race_.NAME.capitalize()} '
                f'{self.class_.NAME.capitalize()}').strip()

    def __repr__(self) -> str:
        """
        Return short description of a character\n
        + stats and characteristics.
        """

        return (
            f'{str(self)}.\n'
            f"{self.get_stat_bar('HP')}\n"
            f"{self.get_stat_bar('SP')}\n"
            f"{self.get_stat_bar('MP')}"
            # f'Stats: {self.get_all_stats()}'
        )

    def __post_init__(self) -> None:
        self.update_actions()
        # update characteristics
        self.health = self.BASE_STATS_MULTIPLIER * self.get_stats('CON')
        self.stamina = self.BASE_STATS_MULTIPLIER * self.get_stats('AGI')
        self.mana = self.BASE_STATS_MULTIPLIER * self.get_stats('INT')


# for testing purpose
if __name__ == '__main__':
    from races import all_races
    from classes import all_classes

    bob = Character('Bob', all_races[2], all_classes[2])
    # print(type(bob.race_).__mro__)
    # print(type(bob.class_).__mro__)
    # print(str(bob.actions))
    # print('-------------------------')
    # rob = Character('Rob', all_races[0], all_classes[0])
    # print(type(rob.race_).__mro__)
    # print(type(rob.class_).__mro__)
    # print(str(rob.actions))
    print(bob.get_stat_bar(left_side=False))

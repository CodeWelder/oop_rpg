"""All types of of creatures stored here as race."""
from dataclasses import dataclass
from typing import ClassVar, Type


@dataclass
class Race():
    """Base class for race."""
    NAME: ClassVar[str] = 'NO RACE'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCPIPTION: ClassVar[bool] = 'NO RACE'

    # the stats will increase character' base stats
    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0,
        'AGI': 0,
        'CON': 0,
        'INT': 0,
        }

    # posible actions
    actions: ClassVar[set[str]] = set()

    def __str__(self) -> str:
        return (f'{self.NAME} - {self.DESCPIPTION}.').capitalize()


@dataclass
class Human(Race):
    """Human race."""
    NAME: ClassVar[str] = 'human'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCPIPTION: ClassVar[bool] = ('diverse and adaptable race, '
                                   'with a wide range of cultural '
                                   'and physical characteristics')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 1,
        'AGI': 1,
        'CON': 1,
        'INT': 1,
        }


@dataclass
class Elf(Race):
    """Elf race."""
    NAME: ClassVar[str] = 'elf'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCPIPTION: ClassVar[bool] = ('a graceful and long-lived race '
                                   'with a deep connection to nature '
                                   'and a talent for magic')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0,
        'AGI': 2,
        'CON': 0,
        'INT': 2,
        }


@dataclass
class Orc(Race):
    """Orc race."""
    NAME: ClassVar[str] = 'orc'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCPIPTION: ClassVar[bool] = ('a powerful and fearsome race '
                                   'known for their physical prowess, '
                                   'fierce demeanor, and often savage '
                                   'culture')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 2,
        'AGI': 0,
        'CON': 2,
        'INT': 0,
        }


@dataclass
class Goblin(Race):
    """Goblin race."""
    NAME: ClassVar[str] = 'goblin'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCPIPTION: ClassVar[bool] = ('a small and cunning race, often '
                                   'found in large groups, with a knack '
                                   'for mechanical and trap-making abilities')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': -2,
        'AGI': 4,
        'CON': -2,
        'INT': 0,
        }


@dataclass
class Rat(Race):
    """Rat race"""
    NAME: ClassVar[str] = 'rat'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCPIPTION: ClassVar[bool] = ('typically viewed as pest or vermin, '
                                   'but may also be used as familiars '
                                   'or as minions of evil wizards, and '
                                   'can possess some surprising cunning '
                                   'and agility')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': -5,
        'AGI': 5,
        'CON': -5,
        'INT': -8,
        }

    actions: ClassVar[set[str]] = {
        'bite',
    }


# make dictionaries for:
# - all race
# - playable race
all_race: dict[str, Type[Race]] = {}
playable_race: dict[str, Type[Race]] = {}
for char_race in Race.__subclasses__():
    if char_race.IS_PLAYABLE:
        playable_race[char_race.NAME] = char_race
    all_race[char_race.NAME] = char_race
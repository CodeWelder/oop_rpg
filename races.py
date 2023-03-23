"""All types of of creatures stored here as race."""
from dataclasses import dataclass
from typing import ClassVar
from character import CharacterAttribute
import actions as act


@dataclass
class Race(CharacterAttribute):
    """Base class for all races."""
    # actions possible for all races
    actions: ClassVar[set[type[act.Action]]] = {
        act.Attack,
        act.Defence,
    }


@dataclass
class Human(Race):
    """Human race."""
    NAME: ClassVar[str] = 'human'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCRIPTION: ClassVar[str] = ('diverse and adaptable race, '
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
    DESCRIPTION: ClassVar[str] = ('a graceful and long-lived race '
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
    DESCRIPTION: ClassVar[str] = ('a powerful and fearsome race '
                                  'known for their physical prowess, '
                                  'fierce demeanor, and often savage '
                                  'culture')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 2,
        'AGI': 0,
        'CON': 2,
        'INT': 0,
        }

    actions: ClassVar[set[type[act.Action]]] = {
        act.Bite,
    }


@dataclass
class Goblin(Race):
    """Goblin race."""
    NAME: ClassVar[str] = 'goblin'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCRIPTION: ClassVar[str] = ('a small and cunning race, often '
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
    DESCRIPTION: ClassVar[str] = ('typically viewed as pest or vermin, '
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

    actions: ClassVar[set[type[act.Action]]] = {
        act.Bite,
    }


# make dictionaries for:
# - all race
# - playable race
all_races: dict[str, CharacterAttribute] = {}
playable_races: dict[str, CharacterAttribute] = {}
for char_race in Race.__subclasses__():
    if char_race.IS_PLAYABLE:
        playable_races[char_race.NAME] = char_race()
    all_races[char_race.NAME] = char_race()

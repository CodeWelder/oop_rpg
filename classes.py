"""Classes of all living creatures in the game"""
from dataclasses import dataclass
from typing import ClassVar, Type


@dataclass
class CharClass():
    """Base class for all characters."""
    # the stats will increase character' base stats
    NAME: str = ''
    IS_PLAYABLE: ClassVar[bool] = False
    DESCPIPTION: ClassVar[str] = ''
    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0,
        'AGI': 0,
        'CON': 0,
        'INT': 0,
        }

    # all posible actions
    actions: ClassVar[set[str]] = set()

    def __str__(self) -> str:
        return (f'{self.NAME} - {self.DESCPIPTION}.').capitalize()


@dataclass
class NoClass(CharClass):
    NAME: ClassVar[str] = 'nobody'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCPIPTION: ClassVar[str] = 'character without class features'

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0,
        'AGI': 0,
        'CON': 0,
        'INT': 0,
        }


@dataclass
class Warrior(CharClass):
    NAME: ClassVar[str] = 'warrior'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCPIPTION: ClassVar[str] = ('a versatile and formidable '
                                  'combatant, skilled '
                                  'in wielding a wide range of '
                                  'weapons and armor to protect '
                                  'allies and vanquish foes')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 2,
        'AGI': 1,
        'CON': 1,
        'INT': 0,
        }

    # actions in addition to the actions available to the parent class
    actions: ClassVar[set[str]] = {
        'increase defence',
    }


@dataclass
class Mage(CharClass):
    NAME: ClassVar[str] = 'mage'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCPIPTION: ClassVar[str] = ('a powerful spellcaster, '
                                  'able to harness arcane energies '
                                  'to cast a variety of spells '
                                  'that can manipulate the elements')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0,
        'AGI': 0,
        'CON': 0,
        'INT': 4,
        }

    # actions in addition to the actions available to the parent class
    actions: ClassVar[set[str]] = {
        'luck',
        'increase attack',
    }


@dataclass
class Thief(CharClass):
    NAME: ClassVar[str] = 'thief'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCPIPTION = ('a small, sneaky creature, '
                   'cunning and vicious')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0,
        'AGI': 2,
        'CON': 1,
        'INT': 1,
        }

    # actions in addition to the actions available to the parent class
    actions: ClassVar[set[str]] = {
        'luck',
    }


# make dictionaries for:
# - all classes
# - playable classes
all_classes: dict[str, Type[CharClass]] = {}
playable_classes: dict[str, Type[CharClass]] = {}
for char_class in CharClass.__subclasses__():
    if char_class.IS_PLAYABLE:
        playable_classes[char_class.NAME] = char_class
    all_classes[char_class.NAME] = char_class

"""Classes of all living creatures in the game"""
from dataclasses import dataclass
from typing import ClassVar
from character import CharacterAttribute
import actions as act


@dataclass
class CharClass(CharacterAttribute):
    """Base class for all characters."""
    pass


@dataclass
class NoClass(CharClass):
    NAME: ClassVar[str] = ''
    IS_PLAYABLE: ClassVar[bool] = False
    DESCRIPTION: ClassVar[str] = 'a character without class features'

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0, 'AGI': 0, 'CON': 0, 'INT': 0,
        }


@dataclass
class Warrior(CharClass):
    NAME: ClassVar[str] = 'warrior'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCRIPTION: ClassVar[str] = ('a versatile and formidable '
                                  'combatant, skilled '
                                  'in wielding a wide range of '
                                  'weapons and armor to protect '
                                  'allies and vanquish foes')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 2, 'AGI': 1, 'CON': 1, 'INT': 0,
        }

    # actions in addition to the actions available to the parent class
    actions: ClassVar[set[type[act.Action]]] = {
        act.Slash,
    }


@dataclass
class Mage(CharClass):
    NAME: ClassVar[str] = 'mage'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCRIPTION: ClassVar[str] = ('a powerful spellcaster, '
                                  'able to harness arcane energies '
                                  'to cast a variety of spells '
                                  'that can manipulate the elements')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0, 'AGI': 0, 'CON': 0, 'INT': 4,
        }

    # actions in addition to the actions available to the parent class
    actions: ClassVar[set[type[act.Action]]] = {
        act.Fireball,
        act.IceShield,
    }


@dataclass
class Thief(CharClass):
    NAME: ClassVar[str] = 'thief'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCRIPTION = ('an agile and skilled at stealing valuable items '
                   'and information while remaining undetected')

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0, 'AGI': 2, 'CON': 1, 'INT': 1,
        }

    # actions in addition to the actions available to the parent class
    actions: ClassVar[set[type[act.Action]]] = {
        act.SmokeBomb,
        act.Backstab,
    }


# make lists of:
# - all classes
# - playable classes
all_classes_types: list[type[CharClass]] = CharClass.__subclasses__()
all_classes: list[CharacterAttribute] = [x() for x in all_classes_types]
playable_classes: list[CharacterAttribute] = list(
    filter(lambda x: x.IS_PLAYABLE, all_classes)
)

# for testing purpose
if __name__ == '__main__':

    mage = Mage()
    print(type(mage).__mro__)
    print(mage.actions)
    thief = Thief()
    print(type(thief).__mro__)
    print(thief.actions)

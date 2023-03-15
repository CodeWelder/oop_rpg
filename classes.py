"""Classes of all living creatures in the game"""
from dataclasses import dataclass
from typing import ClassVar, Type


@dataclass
class Character():
    """Base class for all characters."""
    CLASS_NAME: ClassVar[str] = 'base class'
    IS_PLAYABLE: ClassVar[bool] = False  # is the class playable or not
    CLASS_DESCPIPTION: ClassVar[str] = 'parent class for other classes'
    DEFAULT_ATTACK: ClassVar[int] = 5
    DEFAULT_DEFENCE: ClassVar[int] = 10
    DEFAULT_STAMINA: ClassVar[int] = 80
    ATTACK_VALUE_RANGE: ClassVar[tuple[int, int]]
    DEFENCE_VALUE_RANGE: ClassVar[tuple[int, int]]

    name: str
    is_player: bool = False
    # all posible actions
    possible_actions: ClassVar[set[str]] = {
        'attack',
        'defence',
    }
    # actions in addition to the actions available to the parent class
    unique_actions: ClassVar[set[str]] = set()

    def __post_init__(self) -> None:
        self.possible_actions.update(self.unique_actions)

    def __str__(self) -> str:
        return f'{self.CLASS_NAME} - {self.CLASS_DESCPIPTION}.'


@dataclass
class Warrior(Character):
    CLASS_NAME: ClassVar[str] = 'warrior'
    IS_PLAYABLE: ClassVar[bool] = True
    CLASS_DESCPIPTION: ClassVar[str] = ('versatile and formidable combatant, '
                                        'skilled in wielding a wide range of '
                                        'weapons and armor to protect '
                                        'allies and vanquish foes.')
    ATTACK_VALUE_RANGE: ClassVar[tuple[int, int]] = (3, 5)
    DEFENCE_VALUE_RANGE: ClassVar[tuple[int, int]] = (5, 10)

    # actions in addition to the actions available to the parent class
    unique_actions: ClassVar[set[str]] = {
        'increase defence',
    }


@dataclass
class Mage(Character):
    CLASS_NAME: ClassVar[str] = 'mage'
    IS_PLAYABLE: ClassVar[bool] = True
    CLASS_DESCPIPTION: ClassVar[str] = ('a powerful spellcaster, '
                                        'able to harness arcane energies '
                                        'to cast a variety of spells '
                                        'that can manipulate the elements, '
                                        'control minds, or summon creatures '
                                        'to aid them in battle.')
    ATTACK_VALUE_RANGE: ClassVar[tuple[int, int]] = (5, 10)
    DEFENCE_VALUE_RANGE: ClassVar[tuple[int, int]] = (-2, 2)

    # actions in addition to the actions available to the parent class
    unique_actions: ClassVar[set[str]] = {
        'luck',
        'increase attack',
    }


@dataclass
class Goblin(Character):
    CLASS_NAME: ClassVar[str] = 'goblin'
    IS_PLAYABLE: ClassVar[bool] = False
    CLASS_DESCPIPTION = ('a small, sneaky creature, '
                         'cunning and vicious.')
    ATTACK_VALUE_RANGE: ClassVar[tuple[int, int]] = (5, 10)
    DEFENCE_VALUE_RANGE: ClassVar[tuple[int, int]] = (-2, 2)

    # actions in addition to the actions available to the parent class
    unique_actions: ClassVar[set[str]] = {
        'luck',
    }


# make a dictionaries of classes
all_classes: dict[str, Type[Character]] = {}
playable_classes: dict[str, Type[Character]] = {}
for char_class in Character.__subclasses__():
    if char_class.IS_PLAYABLE:
        playable_classes[char_class.CLASS_NAME] = char_class
    all_classes[char_class.CLASS_NAME] = char_class

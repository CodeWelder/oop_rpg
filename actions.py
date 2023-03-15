"""All actions game characters can do"""
from dataclasses import dataclass
from random import randint
from typing import ClassVar, Optional, Type

from classes import Character


@dataclass
class Action():
    actor: Character
    target: Optional[Character] = None
    NAME: ClassVar[str] = 'default action'
    DESCPIPTION: ClassVar[str] = 'default action'

    def execute(self) -> str:
        return 'Default action executed'


@dataclass
class Attack(Action):
    NAME: ClassVar[str] = 'attack'
    DESCPIPTION: ClassVar[str] = 'to attack the target'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        target_class: str = type(self.target).__name__
        attack_value: int = (self.actor.DEFAULT_ATTACK
                             + randint(*self.actor.ATTACK_VALUE_RANGE))
        return (f'{actor_name} наносит урон {target_class}, '
                f'равный {attack_value}')


@dataclass
class Defence(Action):
    NAME: ClassVar[str] = 'defence'
    DESCPIPTION: ClassVar[str] = 'to defend yourself'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        defence_value: int = (self.actor.DEFAULT_DEFENCE
                              + randint(*self.actor.DEFENCE_VALUE_RANGE))
        return (f'{actor_name} блокирует {defence_value} ед. урона.')


@dataclass
class Luck(Action):
    NAME: ClassVar[str] = 'luck'
    DESCPIPTION: ClassVar[str] = 'to increase your luck'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name}, тебе благоволит удача.')


@dataclass
class IncreaseAttack(Action):
    NAME: ClassVar[str] = 'increase attack'
    DESCPIPTION: ClassVar[str] = 'to increase attack'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} увеличивает атаку.')


@dataclass
class IncreaseDefence(Action):
    NAME: ClassVar[str] = 'increase defence'
    DESCPIPTION: ClassVar[str] = 'to increase defence'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} увеличивает защиту.')


# make a dictionary with all actions
actions: dict[str, Type[Action]] = {}
for action in Action.__subclasses__():
    actions[action.NAME] = action

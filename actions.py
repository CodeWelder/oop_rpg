"""All actions game characters can do"""
from dataclasses import dataclass
# from random import randint
from typing import ClassVar, Optional, Type

from character import Character


@dataclass
class Action():
    actor: Character
    target: Optional[Character] = None
    NAME: ClassVar[str] = 'default action'
    DESCPIPTION: ClassVar[str] = 'default action'

    def execute(self) -> str:
        return 'Default action executed'

    def __str__(self) -> str:
        return (f'{self.NAME} - {self.DESCPIPTION}.').capitalize()


@dataclass
class Attack(Action):
    NAME: ClassVar[str] = 'attack'
    DESCPIPTION: ClassVar[str] = 'to attack your target'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        target_class: str = type(self.target).__name__
        return (f'{actor_name} deals damage {target_class}')


@dataclass
class Defence(Action):
    NAME: ClassVar[str] = 'defence'
    DESCPIPTION: ClassVar[str] = 'to defend yourself'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} blocks all damage.')


@dataclass
class Luck(Action):
    NAME: ClassVar[str] = 'luck'
    DESCPIPTION: ClassVar[str] = 'to increase your luck'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name}, luck favors you.')


@dataclass
class IncreaseAttack(Action):
    NAME: ClassVar[str] = 'increase attack'
    DESCPIPTION: ClassVar[str] = 'to increase attack'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} increases attack.')


@dataclass
class IncreaseDefence(Action):
    NAME: ClassVar[str] = 'increase defence'
    DESCPIPTION: ClassVar[str] = 'to increase defence'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} increases defence.')


@dataclass
class Bite(Action):
    NAME: ClassVar[str] = 'bite'
    DESCPIPTION: ClassVar[str] = 'to bite your target'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} increases defence.')


# make a dictionary with all actions
actions: dict[str, Type[Action]] = {}
for action in Action.__subclasses__():
    actions[action.NAME] = action

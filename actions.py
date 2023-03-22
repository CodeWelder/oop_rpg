"""All actions game characters can do"""
from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character


@dataclass
class Action():
    actor: Character
    target: Character | None = None
    NAME: ClassVar[str] = 'default action'
    DESCPIPTION: ClassVar[str] = 'default action'

    def execute(self) -> str:
        return 'Default action executed'

    def __str__(self) -> str:
        return (f'{self.NAME} - {self.DESCPIPTION}.').capitalize()

    @classmethod
    def describe(cls) -> str:
        return (f'{cls.NAME} - {cls.DESCPIPTION}.').capitalize()


@dataclass
class Attack(Action):
    NAME: ClassVar[str] = 'attack'
    DESCPIPTION: ClassVar[str] = 'to perform standard unarmed attack'

    def execute(self) -> str:
        damage: int = self.actor.get_stats('STR')
        return (f'{str(self.actor)} deals '
                f'{damage} damage to {str(self.target)}')


@dataclass
class Defence(Action):
    NAME: ClassVar[str] = 'defence'
    DESCPIPTION: ClassVar[str] = 'to defend yourself unarmed'

    def execute(self) -> str:
        defence: int = self.actor.get_stats('AGI')
        return (f'{str(self.actor)} blocks '
                f'{defence} damage from {str(self.target)}')


@dataclass
class Slash(Action):
    NAME: ClassVar[str] = 'slash'
    DESCPIPTION: ClassVar[str] = 'to slash your target with melee weapon'

    def execute(self) -> str:
        damage: int = self.actor.get_stats('STR') * 2
        return (f'{str(self.actor)} deals '
                f'{damage} damage to {str(self.target)}')


@dataclass
class Bite(Action):
    NAME: ClassVar[str] = 'bite'
    DESCPIPTION: ClassVar[str] = 'to bite your target'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} increases defence.')


# make a dictionary with all actions
actions: dict[str, type[Action]] = {}
for action in Action.__subclasses__():
    actions[action.NAME] = action

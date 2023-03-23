"""All actions game characters can do"""
from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character


@dataclass
class Action():
    """Base action class."""
    actor: Character
    target: Character | None = None
    NAME: ClassVar[str] = 'default action'
    DESCRIPTION: ClassVar[str] = 'default action'

    def execute(self) -> str:
        return 'Default action executed'

    # for cases when I can't call __str__
    @classmethod
    def describe(cls) -> str:
        """For cases when you can't call __str__."""
        return (f'{cls.NAME} - {cls.DESCRIPTION}.').capitalize()

    def __str__(self) -> str:
        self.describe(type(self))
        # return (f'{self.NAME} - {self.DESCRIPTION}.').capitalize()


@dataclass
class Attack(Action):
    """A standard unarmed attack action class"""
    NAME: ClassVar[str] = 'attack'
    DESCRIPTION: ClassVar[str] = 'to perform standard unarmed attack'

    def execute(self) -> str:
        damage: int = self.actor.get_stats('STR')
        return (f'{str(self.actor)} deals '
                f'{damage} damage to {str(self.target)}')


@dataclass
class Defence(Action):
    NAME: ClassVar[str] = 'defence'
    DESCRIPTION: ClassVar[str] = 'to defend yourself unarmed'

    def execute(self) -> str:
        defence: int = self.actor.get_stats('AGI')
        return (f'{str(self.actor)} blocks '
                f'{defence} damage from {str(self.target)}')


@dataclass
class Slash(Action):
    NAME: ClassVar[str] = 'slash'
    DESCRIPTION: ClassVar[str] = 'to slash your target with melee weapon'

    def execute(self) -> str:
        damage: int = self.actor.get_stats('STR') * 2
        return (f'{str(self.actor)} deals '
                f'{damage} damage to {str(self.target)}')


@dataclass
class Bite(Action):
    NAME: ClassVar[str] = 'bite'
    DESCRIPTION: ClassVar[str] = 'to bite your target'

    def execute(self) -> str:
        actor_name: str = self.actor.name
        return (f'{actor_name} increases defence.')


# make a dictionary with all actions
actions: dict[str, type[Action]] = {}
for action in Action.__subclasses__():
    actions[action.NAME] = action

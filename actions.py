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

    # impact of the action
    damage: ClassVar[int] = 0
    defence: ClassVar[int] = 0

    # cost of the action
    health: ClassVar[int] = 0
    stamina: ClassVar[int] = 0
    mana: ClassVar[int] = 0

    def describe_action(self) -> None:
        """Return action description in a battle."""
        pass

    def execute(self) -> tuple[int, int]:
        self.actor.health += self.health
        self.actor.stamina += self.stamina
        self.actor.mana += self.mana

        impact: tuple[int, int, str] = (
            self.damage,
            self.defence,
            self.describe_action()
        )
        return impact

    def str_(self) -> int:
        return self.actor.get_stats('STR')

    def agi_(self) -> int:
        return self.actor.get_stats('AGI')

    def con_(self) -> int:
        return self.actor.get_stats('CON')

    def int_(self) -> int:
        return self.actor.get_stats('INT')

    @classmethod
    def describe(cls) -> str:
        """For cases when you need description from class
        and you can't call __str__."""
        return (f'{cls.NAME} - {cls.DESCRIPTION}.').capitalize()

    def __str__(self) -> str:
        self.describe(type(self))


@dataclass
class Skip(Action):
    """The service action to exit from while loops"""
    NAME: ClassVar[str] = 'skip'
    DESCRIPTION: ClassVar[str] = 'to skip'

    def describe_action(self) -> None:
        """Return action description in a battle."""
        return 'Doing nothing'


@dataclass
class Attack(Action):
    """A standard unarmed attack action class"""
    NAME: ClassVar[str] = 'attack'
    DESCRIPTION: ClassVar[str] = 'to perform standard unarmed attack'

    def __post_init__(self) -> None:
        # impact of the action
        self.damage = self.str_()
        self.defence = 0
        # cost of the action
        self.health = 0
        self.stamina = -5
        self.mana = 0

    def describe_action(self) -> None:
        """Return action description in a battle."""
        return 'Attacks unarmed - {} damage'.format(self.damage)


@dataclass
class Defence(Action):
    NAME: ClassVar[str] = 'defence'
    DESCRIPTION: ClassVar[str] = 'to defend yourself unarmed'

    def __post_init__(self) -> None:
        # impact of the action
        self.damage = 0
        self.defence = self.agi_()
        # cost of the action
        self.health = 0
        self.stamina = -5
        self.mana = 0

    def describe_action(self) -> None:
        """Return action description in a battle."""
        return 'Defends him/herself - {} defence'.format(self.defence)


@dataclass
class Slash(Action):
    NAME: ClassVar[str] = 'slash'
    DESCRIPTION: ClassVar[str] = 'to slash your target with a melee weapon'

    def __post_init__(self) -> None:
        # impact of the action
        self.damage = self.str_() * 2
        self.defence = 0
        # cost of the action
        self.health = 0
        self.stamina = -7
        self.mana = 0

    def describe_action(self) -> None:
        """Return action description in a battle."""
        return 'Slashes with a weapon - {} damage'.format(self.damage)


@dataclass
class Bite(Action):
    NAME: ClassVar[str] = 'bite'
    DESCRIPTION: ClassVar[str] = 'to bite your target'

    def __post_init__(self) -> None:
        # impact of the action
        self.damage = self.str_()
        self.defence = -5
        # cost of the action
        self.health = 0
        self.stamina = -5
        self.mana = 0

    def describe_action(self) -> None:
        """Return action description in a battle."""
        return 'Bites - {} damage'.format(self.damage)


@dataclass
class Fireball(Action):
    NAME: ClassVar[str] = 'fireball'
    DESCRIPTION: ClassVar[str] = 'to hurl a ball of fire at your target'

    def __post_init__(self) -> None:
        # impact of the action
        self.damage = self.int_() * 3
        self.defence = 0
        # cost of the action
        self.health = 0
        self.stamina = 0
        self.mana = -15

    def describe_action(self) -> None:
        """Return action description in a battle."""
        return 'Hurls a fireball - {} damage.'.format(self.damage)


@dataclass
class IceShield(Action):
    NAME: ClassVar[str] = 'ice shield'
    DESCRIPTION: ClassVar[str] = 'to create a shield of ice around yourself'

    def __post_init__(self) -> None:
        # impact of the action
        self.damage = 0
        self.defence = self.int_() * 2
        # cost of the action
        self.health = 0
        self.stamina = -5
        self.mana = -10

    def describe_action(self) -> None:
        """Return action description in a battle."""
        return 'Creates an ice shield - {} defence.'.format(self.defence)


# make the list of all actions
# all_actions: list[type[Action]] = Action.__subclasses__()
# all_actions: list[Action] = [x() for x in all_actions_types]
if __name__ == '__main__':
    pass

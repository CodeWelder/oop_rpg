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
    DESCRIPTION: ClassVar[str] = (
        'a diverse and adaptable race, '
        'with a wide range of cultural '
        'and physical characteristics'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 1, 'AGI': 1, 'CON': 1, 'INT': 1,
        }


@dataclass
class Elf(Race):
    """Elf race."""
    NAME: ClassVar[str] = 'elf'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCRIPTION: ClassVar[str] = (
        'a graceful and long-lived race '
        'with a deep connection to nature '
        'and a talent for magic'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 0, 'AGI': 2, 'CON': 0, 'INT': 2,
        }


@dataclass
class Orc(Race):
    """Orc race."""
    NAME: ClassVar[str] = 'orc'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCRIPTION: ClassVar[str] = (
        'a powerful and fearsome race '
        'known for their physical prowess, '
        'fierce demeanor, and often savage '
        'culture'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 2, 'AGI': 0, 'CON': 2, 'INT': 0,
        }

    actions: ClassVar[set[type[act.Action]]] = {
        act.Bite,
    }


@dataclass
class Goblin(Race):
    """Goblin race."""
    NAME: ClassVar[str] = 'goblin'
    IS_PLAYABLE: ClassVar[bool] = True
    DESCRIPTION: ClassVar[str] = (
        'a small and cunning race, often '
        'found in large groups, with a knack '
        'for mechanical and trap-making abilities'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': -2, 'AGI': 4, 'CON': -2, 'INT': 0,
        }


@dataclass
class Rat(Race):
    """Rat race."""
    NAME: ClassVar[str] = 'rat'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCRIPTION: ClassVar[str] = (
        'typically viewed as pest or vermin, '
        'but may also be used as familiars '
        'or as minions of evil wizards, and '
        'can possess some surprising cunning '
        'and agility'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': -5, 'AGI': 5, 'CON': -5, 'INT': -8,
        }

    actions: ClassVar[set[type[act.Action]]] = {
        act.Bite,
        act.TailBlow,
    }


@dataclass
class Bear(Race):
    """Bear animal."""
    NAME: ClassVar[str] = 'bear'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCRIPTION: ClassVar[str] = (
        'a large and powerful animal with sharp'
        'claws and teeth, '
        'known for their ferocity and strength'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 4, 'AGI': 0, 'CON': 3, 'INT': -5,
    }

    actions: ClassVar[set[type[act.Action]]] = {
        act.Bite,
        act.Claw,
    }


@dataclass
class Eagle(Race):
    """Eagle animal."""
    NAME: ClassVar[str] = 'eagle'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCRIPTION: ClassVar[str] = (
        'a large bird of prey with sharp talons '
        'and keen eyesight, known for their speed '
        'and agility in the air'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 2, 'AGI': 3, 'CON': 1, 'INT': 0,
    }

    actions: ClassVar[set[type[act.Action]]] = {
        act.Peck,
    }


@dataclass
class Crocodile(Race):
    """Crocodile animal."""
    NAME: ClassVar[str] = 'crocodile'
    IS_PLAYABLE: ClassVar[bool] = False
    DESCRIPTION: ClassVar[str] = (
        'a large reptile with powerful jaws '
        'and tough, scaly skin, known for their '
        'ability to ambush prey in the water'
    )

    BASE_STATS: ClassVar[dict[str, int]] = {
        'STR': 3, 'AGI': 1, 'CON': 3, 'INT': -5,
    }

    actions: ClassVar[set[type[act.Action]]] = {
        act.Bite,
        act.TailBlow,
    }


# make lists of:
# - all races
# - playable races
all_races_types: list[type[Race]] = Race.__subclasses__()
all_races: list[CharacterAttribute] = [x() for x in all_races_types]
playable_races: list[CharacterAttribute] = list(
    filter(lambda x: x.IS_PLAYABLE, all_races)
)

# for testing purpose
if __name__ == '__main__':

    orc = Orc()
    print(type(orc).__mro__)
    print(orc.actions)
    goblin = Goblin()
    print(type(goblin).__mro__)
    print(goblin.actions)

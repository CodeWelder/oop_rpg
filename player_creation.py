from random import choice

from character import Character, CharacterAttribute
from races import playable_races
from classes import playable_classes
from utilities import (
    clear_console,
    enter_some_text,
    choose_from_list,
    generate_name,
)


def create_player() -> Character:
    """The function to control a pipeline
    of player's character creation."""

    # NAME :::::::::::::::::::::::::::::::::::::::::::::::::::::
    clear_console()
    print('Let\'s create your character!')
    char_name: str = enter_some_text()

    # RACE :::::::::::::::::::::::::::::::::::::::::::::::::::::
    header: str = 'Ok, {}! What is your character\'s race?'.format(char_name)
    char_race: CharacterAttribute = choose_from_list(
        playable_races,
        True,
        start_text=header,
    )

    # CLASS ::::::::::::::::::::::::::::::::::::::::::::::::::::
    header: str = 'Well, {} {}! What is your character\'s class?'.format(
        char_race.NAME, char_name,
    )
    char_class: CharacterAttribute = choose_from_list(
        playable_classes,
        True,
        start_text=header,
    )

    # REVIEW AND APPROUVING ::::::::::::::::::::::::::::::::::::
    clear_console()
    char: Character = Character(char_name, char_race, char_class, True)
    print('Look at you, {}'.format(repr(char)))

    # clear_console(initial_print=header)

    approve_choice: str = ''
    approve_choice = input(
        'Enter (y) to confirm your choice or any other button to start over: '
    ).lower()

    clear_console(1)

    if approve_choice == 'y':
        return char
    else:
        return create_player()


def create_random_player():
    player = Character(
        generate_name(),
        choice(playable_races),
        choice(playable_classes),
        False
    )
    return player


# for testing
if __name__ == '__main__':
    create_player()

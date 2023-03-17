import os
from actions import actions
from race import playable_race, Race
from classes import playable_classes, CharClass
from character import Character


def clear_console():
    """Clears console."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def enter_char_name() -> str:
    """
    Asks to enter a name and returns that name.
    """
    approve_choice: str = ''

    while approve_choice != 'y':
        clear_console()
        selected_name: str = input('Enter you character name: ')
        print(f'You name is {selected_name}?')
        approve_choice = input('Enter (y) to confirm your choice '
                               'or any other button to change it: '
                               ).lower()
    return selected_name


def choose_char_race() -> Race:
    """
    Asks to select a race and returns that Race.
    """
    approve_choice: str = ''

    while approve_choice != 'y':
        clear_console()
        print('The following races are available to you:')
        # print available classes string by string
        for race_name in playable_race:
            text: str = (
                f'{playable_race[race_name].NAME} - '
                f'{playable_race[race_name].DESCPIPTION}'
            ).capitalize()
            print(text)

        # ask to choose a class
        selected_race: str = input('Enter a race of the character '
                                   'you want to play: ').lower()
        clear_console()
        # if selected class is available
        if selected_race in playable_race:
            # create a player character
            char_race: Race = playable_race[selected_race]()
            # print what is selected
            print(f'You have selected a race:\n{char_race}')
            # ask for approve
            approve_choice = input('Enter (y) to confirm your choice '
                                   'or any other button to change it: '
                                   ).lower()
            clear_console()

    return char_race


def choose_char_class() -> CharClass:
    """
    Asks to select a class and returns that  class.
    """
    approve_choice: str = ''

    while approve_choice != 'y':
        clear_console()
        print('The following classes are available to you:')
        # print available classes string by string
        for class_name in playable_classes:
            text: str = (
                f'{playable_classes[class_name].NAME} - '
                f'{playable_classes[class_name].DESCPIPTION}'
            ).capitalize()
            print(text)

        # ask to choose a class
        selected_class: str = input('Enter a class of the character '
                                    'you want to play: ').lower()
        clear_console()
        # if selected class is available
        if selected_class in playable_classes:
            # create a player character
            char_class: CharClass = playable_classes[selected_class]()
            # print what is selected
            print(f'You have selected a class:\n{char_class}')
            # ask for approve
            approve_choice = input('Enter (y) to confirm your choice '
                                   'or any other button to change it: '
                                   ).lower()
            clear_console()

    return char_class


def start_training(character: Character) -> str:
    """
    Takes as input a character object created in choice_char_class.
    Returns messages about the results of a character's training cycle.
    """

    # get the actions available to the character
    char_actions: list[str] = list(character.actions)
    # and sort them
    char_actions.sort()

    print('Practice to control your character.')
    # print available actions string by string
    for action in char_actions:
        text: str = (
            f'{actions[action].NAME} - '
            f'{actions[action].DESCPIPTION}'
        ).capitalize()
        print(text)

    print('If you do not want to train, enter "skip".')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Enter command: ').lower()
        # if the command is in the command list
        # the class method which matches the given command
        # will be called in the print() function.
        if cmd in actions and cmd in char_actions:
            selected_action = actions[cmd](character).execute()
            print(selected_action)

    return 'Training is over.'


if __name__ == '__main__':
    player = Character(enter_char_name(),
                       choose_char_race(),
                       choose_char_class(),
                       True)
    start_training(player)

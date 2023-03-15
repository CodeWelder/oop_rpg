import os
from actions import actions
from classes import Character, playable_classes


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def choice_char_class(char_name: str) -> Character:
    """
    Returns the selected character class.
    """
    clear_console()
    approve_choice: str = ''

    while approve_choice != 'y':

        # print available classes string by string
        print('Available classes:')
        for class_name in playable_classes:
            text: str = (
                f'{playable_classes[class_name].CLASS_NAME} - '
                f'{playable_classes[class_name].CLASS_DESCPIPTION}'
            ).capitalize()
            print(text)

        # ask to choose a class
        selected_class: str = input('Enter the class of the character '
                                    'you want to play: ').lower()
        clear_console()
        # if selected class is available
        if selected_class in playable_classes:
            # create a player character
            char_class: Character = playable_classes[selected_class](char_name)
            # print what is selected
            print(f'You have selected a class:\n{char_class}')
            # ask for approve
            approve_choice = input('Enter (Y) to confirm your choice '
                                   'or any other button '
                                   'to select a different class: '
                                   ).lower()
            clear_console()
        # if selected class is NOT available
        else:
            print('Choose a class from the list of available.')

    return char_class


def start_training(character: Character) -> str:
    """
    Takes as input a character object created in choice_char_class.
    Returns messages about the results of a character's training cycle.
    """

    # get the actions available to the character
    possible_actions: list[str] = list(character.possible_actions)
    # and sort them
    possible_actions.sort()

    print('Practice to control your character.')
    # print available actions string by string
    for action in possible_actions:
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
        if cmd in actions and cmd in possible_actions:
            selected_action = actions[cmd](character).execute()
            print(selected_action)
        else:
            print(f'There is no such command like "{cmd}"')
    return 'Training is over.'


start_training(choice_char_class('Some_name'))

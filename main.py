import os
from actions import Action
from races import playable_races
from classes import playable_classes
from character import Character, CharacterAttribute
import text


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


def choose_from(
        options: dict[str, type[CharacterAttribute]]
        ) -> type[CharacterAttribute]:
    """
    Print descriptions of values from a dictionary.
    Ask to choose one of them.
    Return chosen value.
    """
    approve_choice: str = ''

    while approve_choice != 'y':
        clear_console()
        print('The following options are available to you:')
        print(text.HORIZONTAL_LINE)
        # print all options in separate lines
        for option in options:
            description: str = str(options[option].describe())
            print(description)

        print(text.HORIZONTAL_LINE)
        chosen: str = input('Enter your choice: ').lower()
        clear_console()

        # if selected class is available
        if chosen in options:
            result: type[CharacterAttribute] = options[chosen]
            print('You have chosen:')
            print(result.describe())
            print(text.HORIZONTAL_LINE)
            approve_choice = input('Enter (y) to confirm your choice '
                                   'or any other button to change it: '
                                   ).lower()
            clear_console()

    return result


def start_training(character: Character) -> str:
    """
    Takes as input a character instance.
    Returns messages about the results of a character's training cycle.
    """

    # construct dict of actions available to the character
    actions_dict: dict[str, type[Action]] = dict()
    for action in character.actions:
        actions_dict[action.NAME] = action

    print('The following options are available to you:')
    print(text.HORIZONTAL_LINE)

    # print available actions string by string
    for action in character.actions:
        print(action.describe())
    print('Skip - if you do not want to train.')
    print(text.HORIZONTAL_LINE)

    chosen: str = ''
    while chosen != 'skip':
        chosen = input('Enter command: ').lower()
        # if the command is in the command list
        # the class method which matches the given command
        # will be called in the print() function.
        if chosen in actions_dict:
            selected = actions_dict[chosen](character).execute()
            print(selected)

    return 'Training is over.'


if __name__ == '__main__':
    player = Character(enter_char_name(),
                       choose_from(playable_races),
                       choose_from(playable_classes),
                       True)
    start_training(player)

    # bob = Character('Bob', all_race['rat'], all_classes['warrior'])
    # alice = Character('Alice', all_race['goblin'], all_classes['mage'])
    # print(actions['attack'](bob, alice).execute())
    # print(actions['defence'](alice, bob).execute())

import os
from random import choice

from names import names_list
import text


def clear_console(lines_to_erase: int = 0, initial_print: str = ''):
    """
    Clears console:\n
    If lines_to_erase == 0 - clears all,\n
    if lines_to_erase >= 1 - clears the number of lines in console.\n
    Prints initial print after that.
    """
    if lines_to_erase == 0:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    elif lines_to_erase >= 1:
        print(f'\033[{lines_to_erase}A\033[0J', end='')
    print(initial_print, end='')


def close_game():
    """Close the game script."""
    # Going to somthing here in the future
    quit()


def generate_name():
    """
    Takes 2 names from long names list
    and fuses them to make new name.
    """
    first_part: str = choice(names_list)[:3]
    second_part: str = choice(names_list)[3:]
    generated_name = f'{first_part}{second_part}'
    return generated_name


def choose_from_list(
    options: list[any],
    need_approvement: bool = False,
    start_text: str = 'The following options are available to you.',
) -> any:
    """
    Print descriptions of values from a dictionary.
    Ask to choose one of them by number.
    Return chosen value.
    Ask to approve if need_approvement == True.
    """
    # Index in list of options starts from 0,
    # but we want to show the list like it starts from 1.
    INDEX_CORRECTION: int = 1

    approve_choice: str = ''
    while approve_choice != 'y':
        clear_console()
        print(start_text)
        print(text.HORIZONTAL_LINE)

        # print all options' descriptions in separate lines
        for i, option in enumerate(options):
            description: str = ''
            try:
                # for class' types used methode describe()
                description = option.describe()
            except AttributeError:
                description: str = str(option)
            # +1 here to start printed list from 1
            print(f'{i + INDEX_CORRECTION}. {description}')

        print(text.HORIZONTAL_LINE)
        chosen: int = -1  # just a number that can't be list's index
        try:
            # -1 here to match chosen number with actual list' index
            chosen = int(input('Enter your choice #: ')) - INDEX_CORRECTION
        except ValueError:
            pass

        # if selected is available
        if chosen in range(len(options)):
            result: any = options[chosen]
            print('You have chosen:')
            print(str(result))
            print(text.HORIZONTAL_LINE)

            if need_approvement:
                approve_choice = input(
                    'Enter (y) to confirm your choice '
                    'or any other button to change it: '
                ).lower()
            else:
                approve_choice = 'y'

    return result


def enter_some_text(
    start_text: str = 'Enter your character name: ',
    end_text: str = 'You name is {}?'
) -> str:
    """Asks to enter some text and returns it."""
    approve_choice: str = ''
    while approve_choice != 'y':
        entered_text: str = input(start_text)
        # print(f'You name is {selected_name}?')
        print(end_text.format(entered_text))
        approve_choice = input(
            'Enter (y) to confirm your choice '
            'or any other button to change it: '
        ).lower()
        clear_console(3)
    return entered_text

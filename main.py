import os
from random import choice

# from actions import Action
from races import playable_races
from classes import playable_classes
from character import Character, CharacterAttribute
from names import names_list
from battle import print_round_header, strings_to_edges
import text


def clear_console(lines_to_erase: int = 0, initial_print: str = ''):
    """
    Clears console:\n
    If lines_to_erase == 0 - clears all, and prints initial_print\n
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


def enter_char_name() -> str:
    """Asks to enter a name and returns that name."""
    approve_choice: str = ''
    while approve_choice != 'y':
        selected_name: str = input('Enter your character name: ')
        print(f'You name is {selected_name}?')
        approve_choice = input('Enter (y) to confirm your choice '
                               'or any other button to change it: '
                               ).lower()
        clear_console(3)
    return selected_name


def generate_name():
    first_part: str = choice(names_list)[:3]
    second_part: str = choice(names_list)[3:]
    generated_name = f'{first_part}{second_part}'
    return generated_name


def choose_from_list(
        options: list[any],
        need_approvement: bool = False,
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
        # print('The following options are available to you:')
        print(text.HORIZONTAL_LINE)
        # print all options' descriptions in separate lines
        # for class' types used methode describe()
        for i, option in enumerate(options):
            description: str = ''
            try:
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
        # clear_console()

        # if selected is available
        if chosen in range(len(options)):
            result: any = options[chosen]
            print('You have chosen:')
            print(str(result))
            print(text.HORIZONTAL_LINE)

            if need_approvement:
                approve_choice = input('Enter (y) to confirm your choice '
                                       'or any other button to change it: '
                                       ).lower()
            else:
                approve_choice = 'y'
        # clear_console()

    return result


def create_player() -> Character:
    """The function to control a pipeline
    of player's character creation."""

    # NAME
    header: str = 'Let\'s create your character!\n'
    clear_console(initial_print=header)
    char_name: str = enter_char_name()

    # RACE
    header = 'Ok, {}! What is your character\'s race?\n'.format(char_name)
    clear_console(initial_print=header)
    char_race: CharacterAttribute = choose_from_list(playable_races, True)

    # CLASS
    header = 'Well, {} {}! What is your character\'s class?\n'.format(
        char_race.NAME,
        char_name
    )
    clear_console(initial_print=header)
    char_class: CharacterAttribute = choose_from_list(playable_classes, True)

    # REVIEW AND APPROUVING
    char: Character = Character(char_name, char_race, char_class, True)
    header = ('Look at you, {}\n'
              ).format(repr(char))
    clear_console(initial_print=header)

    approve_choice: str = ''
    approve_choice = input('Enter (y) to confirm your choice '
                           'or any other button to start over: '
                           ).lower()
    clear_console(1)

    if approve_choice == 'y':
        return char
    else:
        return create_player()


# def start_training(character: Character) -> None:
#     """
#     Takes as input a character instance.
#     Returns messages about the results of a character's training cycle.
#     """
#     chosen: str = ''
#     while chosen != 'skip':
#         chosen: type[Action] = choose_from_list(
#             character.get_actions_list(),
#             False
#             )
#         text: str = chosen(character, None).execute()
#         print(text)

#     print('Training is over.')


if __name__ == '__main__':

    # 1 MAIN MENU
    clear_console()
    print('OOP RPG')
    choose_from_list(['New game', 'Load game', 'Exit'])  # REFACTOR
    clear_console()

    # 2 PLAYER CREATION
    player = create_player()
    clear_console()
    print(player)

    # 3 DIRECTION CHOICE
    direction = choose_from_list(['North', 'South', 'West', 'East'])
    clear_console()
    print(f'You chose to go {direction}')

    # random player for tests
    # player = Character(
    #     generate_name(),
    #     choice(playable_races),
    #     choice(playable_classes),
    #     False
    # )

    # 4 ENEMY GENERATION
    enemy = Character(
        generate_name(),
        choice(playable_races),
        choice(playable_classes),
        False
    )

    # 5 BATTLE
    print(f'On your way you meet {enemy}')
    print('Let the battle begin!')
    round_: int = 0
    print_round_header(player, enemy, round_)
    while player.health > 0 and enemy.health > 0:

        # player_choice = choice(list(player.actions))
        player_choice = choose_from_list(
            player.get_actions_list(),
            False
        )
        enemy_choice = choice(list(enemy.actions))

        # tuple(self.damage, self.defence)
        player_turn = player.perform_action(
            player_choice,
            enemy
        )
        clear_console()

        enemy_turn = enemy.perform_action(
            enemy_choice,
            player
        )
        print_round_header(player, enemy, round_)
        print(strings_to_edges(player_turn[2], enemy_turn[2]))

        player_damage_str: str = 'Takes no damage.'
        if player_turn[1] < enemy_turn[0]:
            damage_taken = enemy_turn[0] - player_turn[1]
            player_damage_str = f'Takes {damage_taken} damage.'
            player.health -= damage_taken

        enemy_damage_str: str = 'Takes no damage.'
        if enemy_turn[1] < player_turn[0]:
            damage_taken = player_turn[0] - enemy_turn[1]
            enemy_damage_str = f'Takes {damage_taken} damage.'
            enemy.health -= damage_taken

        print(strings_to_edges(player_damage_str, enemy_damage_str))

        round_ += 1
    clear_console()
    print_round_header(player, enemy, round_)
    print(strings_to_edges(player_turn[2], enemy_turn[2]))

    if player.health <= 0:
        message = 'You was defeted!'
    else:
        message = f'{enemy} was defeted!'

    print(message.center(80))

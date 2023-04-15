from random import choice
from time import sleep

# from actions import Action
from utilities import (
    clear_console,
    close_game,
    generate_name,
    choose_from_list,
)
from player_creation import create_player, create_random_player
from races import all_races
from classes import all_classes
from character import Character

from battle import get_round_header, strings_to_edges


def enter_char_name() -> str:
    """Asks to enter a name and returns that name."""
    approve_choice: str = ''
    while approve_choice != 'y':
        selected_name: str = input('Enter your character name: ')
        print(f'You name is {selected_name}?')
        approve_choice = input(
            'Enter (y) to confirm your choice '
            'or any other button to change it: '
        ).lower()
        clear_console(3)
    return selected_name


if __name__ == '__main__':

    # 1 MAIN MENU ::::::::::::::::::::::::::::::::::::::::::::::
    menu_choice = choose_from_list(
        start_text='OOP RPG',
        options=[
            'New game',
            'Load game - DOES NOT WORK',
            'Exit',
        ],
    )

    if menu_choice == 'Exit':
        close_game()

    # 2 PLAYER CREATION ::::::::::::::::::::::::::::::::::::::::
    player = create_player()

    # player = create_random_player()

    # 3 DIRECTION CHOICE
    direction = choose_from_list(
        [
            'North',
            'South',
            'West',
            'East',
            'Exit game',
        ]
    )

    if direction == 'Exit game':
        close_game()

    clear_console()
    print(f'You chose to go {direction}')

    # 4 ENEMY GENERATION
    # enemy = Character(
    #     generate_name(),
    #     choice(playable_races),
    #     choice(playable_classes),
    #     False
    # )

    enemy = Character(
        generate_name(),
        choice(all_races),
        choice(all_classes),
        False
    )

    # 5 BATTLE
    clear_console()
    print(f'On your way you meet {enemy}'.center(80))
    print('Let the battle begin!'.center(80))
    sleep(2)

    round_: int = 0
    actions_line: str = ''
    damage_line: str = ''
    header: str = get_round_header(player, enemy, round_)

    def get_round_stats() -> str:
        round_stats = (
            f'{get_round_header(player, enemy, round_)}\n'
            f'{actions_line}\n'
            f'{damage_line}'
        )
        return round_stats

    while player.health > 0 and enemy.health > 0:

        player_choice = choose_from_list(
            player.get_actions_list(),
            False,
            start_text=get_round_stats(),
        )
        enemy_choice = choice(list(enemy.actions))

        # perform action returns tuple(self.damage, self.defence)
        player_turn = player.perform_action(
            player_choice,
            enemy
        )
        enemy_turn = enemy.perform_action(
            enemy_choice,
            player
        )

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

        header = get_round_header(player, enemy, round_)
        actions_line = strings_to_edges(player_turn[2], enemy_turn[2])
        damage_line = strings_to_edges(player_damage_str, enemy_damage_str)

        round_ += 1

    clear_console()
    print(get_round_stats())

    if player.health <= 0:
        message = 'You was defeted!'
    else:
        message = f'{enemy} was defeted!'

    print(message.center(80))

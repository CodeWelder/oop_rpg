from character import Character


SCREEN_WIDTH: int = 80


def strings_to_edges(
    string1: str = '',
    string2: str = '',
    screen_width: int = SCREEN_WIDTH,
    border_symbol: str = '|',
    filler: str = ' ',
) -> str:
    """
    Return string formatted like this:\n
    |Bob the Human Warrior___________________Nick the Orc Mage|
    """
    screen_no_border_width: int = screen_width - 2  # 2 borders: left and right
    padding_width: int = screen_no_border_width - len(string1) - len(string2)
    padding: str = filler * padding_width
    result: str = f'{border_symbol}{string1}{padding}{string2}{border_symbol}'
    return result


def print_round_header(
    char1: Character,
    char2: Character,
    round_numder: int
) -> None:
    """
    Prints a header like this:\n
     _________________________________________________________ \n
    |Bob the Human Warrior___________________Nick the Orc Mage|\n
    |HP ██████████ 100_________________________90 █████████ HP|\n
    |SP ░░░░░░░░░ 90 ___________________________80 ░░░░░░░░ SP|\n
    |MP ▓▓▓▓▓▓▓▓▓▓ 100____________________________60 ▓▓▓▓▓▓ MP|\n
    |_________________________________________________________|.
    """

    round_text: str = f' Round {round_numder} '
    # horizontal borders
    H_BORDER_UP: str = f'{round_text.center(SCREEN_WIDTH, ":")}'
    H_BORDER_DOWN: str = strings_to_edges(filler='_')

    # Names line
    char1_name: str = str(char1)
    char2_name: str = str(char2)
    names_line: str = strings_to_edges(char1_name, char2_name)
    # Health line
    char1_health_bar: str = f'HP {int(char1.health / 5) * "█"} {char1.health}'
    char2_health_bar: str = f'{char2.health} {int(char2.health / 5) * "█"} HP'
    health_line: str = strings_to_edges(char1_health_bar, char2_health_bar)
    # Stamina line
    char1_stamina_bar: str = (
        f'SP {int(char1.stamina / 5) * "░"} '
        f'{char1.stamina}'
    )
    char2_stamina_bar: str = (
        f'{char2.stamina} '
        f'{int(char2.stamina / 5) * "░"} SP'
    )
    stamina_line: str = strings_to_edges(char1_stamina_bar, char2_stamina_bar)
    # Mana line
    char1_mana_bar: str = (
        f'MP {int(char1.mana / 5) * "▓"} '
        f'{char1.mana}'
    )
    char2_mana_bar: str = (
        f'{char2.mana} '
        f'{int(char2.mana / 5) * "▓"} MP'
    )
    mana_line: str = strings_to_edges(char1_mana_bar, char2_mana_bar)

    header_to_print: str = (
        f'{H_BORDER_UP}\n'
        f'{names_line}\n'
        f'{health_line}\n'
        f'{stamina_line}\n'
        f'{mana_line}\n'
        f'{H_BORDER_DOWN}'
    )

    print(header_to_print)

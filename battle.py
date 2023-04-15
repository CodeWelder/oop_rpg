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


def get_stat_bar(
    char: Character,
    stat: str = 'HP',
    left_side: bool = True,
) -> str:
    """Returns bar of HP (health), SP (stamina) or MP (mana)."""
    BAR_RESOLUTION: int = 5

    stat_value_mapping: dict[str, int] = {
        'HP': char.health,
        'SP': char.stamina,
        'MP': char.mana,
    }
    stat_symbol_mapping: dict[str, str] = {
        'HP': '█',
        'SP': '░',
        'MP': '▓',
    }

    stat_value: int = stat_value_mapping[stat]
    stat_symbol: str = stat_symbol_mapping[stat]
    bar: str = int(stat_value / BAR_RESOLUTION) * stat_symbol
    result: str = ''

    if left_side is True:
        result: str = f'{stat} {bar} {stat_value}'
    else:
        result: str = f'{stat_value} {bar} {stat}'

    return result


def get_round_header(
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
    char1_health_bar: str = get_stat_bar(char1, 'HP')
    char2_health_bar: str = get_stat_bar(char2, 'HP', False)
    health_line: str = strings_to_edges(char1_health_bar, char2_health_bar)

    # Stamina line
    char1_stamina_bar: str = get_stat_bar(char1, 'SP')
    char2_stamina_bar: str = get_stat_bar(char2, 'SP', False)
    stamina_line: str = strings_to_edges(char1_stamina_bar, char2_stamina_bar)

    # Mana line
    char1_mana_bar: str = get_stat_bar(char1, 'MP')
    char2_mana_bar: str = get_stat_bar(char2, 'MP', False)
    mana_line: str = strings_to_edges(char1_mana_bar, char2_mana_bar)

    header_to_print: str = (
        f'{H_BORDER_UP}\n'
        f'{names_line}\n'
        f'{health_line}\n'
        f'{stamina_line}\n'
        f'{mana_line}\n'
        f'{H_BORDER_DOWN}'
    )

    return header_to_print

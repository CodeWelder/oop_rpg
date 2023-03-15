from actions import actions
from classes import Character, playable_classes


def start_training(character: Character) -> str:
    """
    Принимает на вход объект персонажа, созданный в choice_char_class.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """

    # достаем действия доступные персонажу
    possible_actions: list[str] = list(character.possible_actions)
    # и сортируем их
    possible_actions.sort()

    print('Потренируйся управлять своими навыками.')
    # выводит действия, доступные персонажу
    for action in possible_actions:
        text: str = (
            f'{actions[action].NAME} - '
            f'{actions[action].DESCPIPTION}'
        ).capitalize()
        print(text)

    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ').lower()
        # если команда в перечне команд
        # В функции print() будет вызываться метод класса
        # который соответствует введённой команде.
        if cmd in actions and cmd in possible_actions:
            selected_action = actions[cmd](character).execute()
            print(selected_action)
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает выбранный класс персонажа.
    """

    approve_choice: str = ''

    while approve_choice != 'y':
        print('Доступные классы:')
        # выводим классы, доступные персонажу
        for class_name in playable_classes:
            text: str = (
                f'{playable_classes[class_name].CLASS_NAME} - '
                f'{playable_classes[class_name].CLASS_DESCPIPTION}'
            ).capitalize()
            print(text)

        selected_class: str = input('Введи класс персонажа, '
                                    'за которого хочешь играть: ')
        if selected_class in playable_classes:
            char_class: Character = playable_classes[selected_class](char_name)
            # Вывели в терминал описание персонажа.
            print(char_class)
            approve_choice = input('Введи (Y), чтобы подтвердить выбор, '
                                   'или любую другую кнопку, '
                                   'чтобы выбрать другой класс '
                                   ).lower()
        print('Выберите класс из перечня доступных.')

    return char_class


start_training(choice_char_class('Some_name'))

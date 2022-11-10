SIZE = 3
FIRST_PLAYER_SYMBOL = "x"
SECOND_PLAYER_SYMBOL = "0"
EMPTY_CEIL = None


def main():
    field = init_field(SIZE)
    player = FIRST_PLAYER_SYMBOL
    current_player = get_symbol(input("Введите кто первый ходит (1 - 'x', 2 - '0')\n"))
    if current_player == 1:
        player = "x"
    if current_player == 2:
        player = "0"
    while True:
        step = player_step(field)
        field[step[0]][step[1]] = player
        show_field(field)
        if is_win(field):
            print(f"Выиграл {player}")
            break
        if not has_empty_ceil(field):
            print(f"Ничья")
            break
        player = "0" if player == "x" else "x"


def init_field(size: int = 3) -> list[list]:
    """
    Инициализация поля
    :param size: Размер поля
    :return: Поле заполненное пустыми ячейками
    """
    field = [[EMPTY_CEIL] * size for _ in range(size)]
    return field


def show_field(field: list[list]) -> None:
    """
    Функция показывает состояние поля
    :param field: объект структуры поля
    :return: отображает поле в процессе игры
    """
    for row in field:
        for cell in row:
            if cell is EMPTY_CEIL:
                cell = " "
            print(f"|{cell}", end="")
        print("|")


def player_step(field: list[list]):
    """ Функция показывает ход игрока """
    while True:
        try:
            x = int(input("Введите строку\n"))
        except ValueError:
            print("Введите еще раз")
            continue
        if not 1 <= x <= SIZE:
            print("Не правильно")
            continue
        try:
            y = int(input("Введите столбец\n"))
        except ValueError:
            print("Введите еще раз")
            continue
        if not 1 <= y <= SIZE:
            print("Не правильно")
            continue
        current_row = field[x - 1]
        current_cell = current_row[y - 1]
        if current_cell != EMPTY_CEIL:
            print("Координата занята")
            continue
        cell_number = (x - 1, y - 1)
        return cell_number


def get_ceil(field, cell_number):
    """Получаем ячейку"""
    return field[cell_number[0] - 1][cell_number[1] - 1]


def has_empty_ceil(field):
    """Проверка есть ли еще пустые ячейки"""
    for row in field:
        for cell in row:
            if cell is EMPTY_CEIL:
                return True
    return False


def get_symbol(val):
    if val == 1:
        return "x"
    elif val == 2:
        return "0"
    return EMPTY_CEIL


def is_win(field:list[list]) -> bool:
    """ Функция показывает есть ли выигрышные коомбинации """
    win_comb = [
        # По диагонали
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        # По вертикали
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # По горизонтали
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)]
        ]

    for comb in win_comb:
        ceil_1 = get_ceil(field, comb[0])
        ceil_2 = get_ceil(field, comb[1])
        ceil_3 = get_ceil(field, comb[2])
        if ceil_1 == ceil_2 == ceil_3 != EMPTY_CEIL:
            return True
    return False


if __name__ == '__main__':
    main()

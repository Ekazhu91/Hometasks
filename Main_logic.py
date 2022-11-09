SIZE = 3
FIRST_PLAYER_SYMBOL = "0"
SECOND_PLAYER_SYMBOL = "x"
EMPTY_CEIL = None


def main():
    field = init_field(SIZE)
    print_field(field)

    while True:
        player_step(field, FIRST_PLAYER_SYMBOL)
        if is_win(field):
            break
        print_field(field)
        if  not has_empty_ceil:
            break

        enemy_step(field, SECOND_PLAYER_SYMBOL)
        if is_win(field):
            break
        print_field(field)
        if  not has_empty_ceil:
            break


def init_field(size: int = 3) -> list[list]:
    """
    Инициализация поля
    :param size: Размер поля
    :return: Поле заполненное пустыми ячейками
    """
    field = [[EMPTY_CEIL] * size for _ in range(size)]
    return field


def show_field(field:str, cols=3):
    """
    Функция показывает состояние поля
    :param field: объект структуры поля
    :return: отображает поле в процессе игры
    """
    for idx, val in enumerate(field):
        if idx % cols != 0 or idx == 0:
           print(f"|{get_symbol(val)}", end="")
        else:
            print(f"|\n{get_symbol(val)}", end="")
    print("|")


def player_step(field: list[list]):
    while True:
        try:
            x = int(input("Введите x"))
        except ValueError:
            print("Введите еще раз")
            continue
        if not 1 <= x <= SIZE:
            print("Не правильно")
            continue
        try:
            y = int(input("Введите y"))
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


def get_cell(field, cell_number):
    """Получаем ячейку"""
    return field[cell_number[0] - 1][cell_number[1] - 1]


def has_empty_ceil(ceil_number,field) -> bool:
    """
    Проверка занятости конкретной ячейки

    :param ceil_number:
    :param field:
    :return: Ячейка пустая или нет
    """
    for row in field:
        for ceil in row:
            if ceil is EMPTY_CEIL:
                return True
    return False


def get_symbol(val):
    if val == 1:
        return "x"
    elif val == 2:
        return "0"
    return EMPTY_CEIL


def enemy_step(field, player_symbol):
    player_step(field, player_symbol)


def is_win(field):
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
        coord_1, coord_2, coord_3 = 0  # КАКИЕ КООРДИНАТЫ ЗДЕСЬ УКАЗАТЬ?
        ceil_1 = get_ceil(fiel, coord_1)
        ceil_2 = get_ceil(fiel, coord_2)
        ceil_3 = get_ceil(fiel, coord_3)

        if ceil_1 == ceil_2 == ceil_3 != EMPTY_CEIL:
            return True


if __name__ == '__main__':
    main()

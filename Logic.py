EMPTY_CEIL = None


def init_field(size: int = 3) -> list[list]:
    """
    Инициализация поля

    :param size: Размер поля
    :return: Поле заполненное пустыми ячейками
    """
    return [

        [EMPTY_CEIL] * size for _ in range(size)
    ]

def set_ceil(field: list[list], ceil_number, player_symbol):
    """
    Установка значения в ячейку

    :param field:
    :param ceil_number:
    :param player_symbol:
    :return:
    """

def get_ceil(field: list[list], ceil_number):

def is_empty_ceil(field, ceil_number: tuple) -> bool:
    """
        Проверка занятости конкретной ячейки

        :param ceil_number:
        :param field:
        :return: Ячейка пустая или нет
        """
    current_ceil = get_ceil(field, ceil_number)

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


def is_win(fiel):
    win_comb = [
        # По диагонали
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        # По вертикали
        [(0, 0),( 0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # По горизонтали
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)]
    ]
    coord_1, coord_2, coord_3 = #какие координаты тут указать?
    ceil_1 = get_ceil(fiel, coord_1)
    ceil_2 = get_ceil(fiel, coord_2)
    ceil_3 = get_ceil(fiel, coord_3)

    if ceil_1 == ceil_2 == ceil_3 != EMPTY_CEIL:
        return True




def get_symbol(val):
    if val == "0":
        return " "
    elif val == "1":
        return "X"
    return "0"

def change_player():

def get_first_player():


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

def inif_field(size: int = 3) -> list[list]:
    """ Инициализация поля """


if __name__ == '__main__':
    field = "101011222"
    show_field(field)

#Инициализация игроков
player1 = 1 # Крестик
player2 = 2 # Нолик

def who_win(field, len_seq):
    pass



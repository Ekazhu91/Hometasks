from Logic import init_field, has_empty_ceil, is_empty_ceil

SIZE = 3
FIRST_PLAYER_SYMBOL = "0"
SECOND_PLAYER_SYMBOL = "x"


def print_field(field):
    print()


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


def player_step(field: list[list], player_symbol):
    while True:
        try:
            x = int(input("Введите x"))
        except ValueError:
            print("Введите еще раз")
            continue

        if not 1 <= x <= SIZE:
            print("Не правильно")
            continue



    while True:
        try:
            y = int(input("Введите y"))
        except ValueError:
            print("Введите еще раз")
            continue

        if not 1 <= y <= SIZE:
            print("Не правильно")
            continue

    is_empty_ceil(field, (x, y))


def enemy_step(field, player_symbol):
    player_step(field, player_symbol)


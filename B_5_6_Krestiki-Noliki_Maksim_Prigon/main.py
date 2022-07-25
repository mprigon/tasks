# игра крестики - нолики на поле 3 * 3
# итоговое задание по модулю B5.6
# выполнил Пригон Максим, FPW - 82

# функция печати поля игры с оболочкой в консоль
def print_field(m_):
    m_to_print = m_[:]
    # оболочка поля
    list_0 = ['0', '1', '2']
    list_1 = [' ', '0', '1', '2']

    for n in range(0, 3):
        m_to_print[n].insert(0, list_0[n])

    m_to_print.insert(0, list_1)

    for row_ in m_to_print:
        for column_ in row_:
            print(column_, end='  ')
        print()

    # убираем оболочку
    m_to_print.pop(0)
    for n in range(0, 3):
        m_to_print[n].pop(0)

    return 0


# функция возвращает список [строка, столбец] текущего хода и проверяет
# корректность ввода
# передача player1_moves_, player2_moves_ нужна для вызова функции, проверяющей, был ли уже такой ход
def move_(player_name, player1_moves_, player2_moves_):
    # insert_move - список строковых переменных хода

    print(f'{player_name}, введите свой ход')
    insert_move = list(map(str, input('номер строки и номер '
                                      'столбца, между ними пробел:').split()))

    # проверка ввода двух аргументов
    inserted_ = len(insert_move)
    if inserted_ != 2:
        while inserted_ != 2:
            print('некорректный ход, должно быть два аргумента, введите заново')
            insert_move = list(map(str, input('номер строки и номер '
                                              'столбца, между ними пробел:').split()))
            inserted_ = len(insert_move)

    # введено два аргумента, теперь проверка ввода цифр, а не букв
    insert_move_str = ''.join(insert_move)
    is_digit = insert_move_str.isdigit()
    if not is_digit:
        while not is_digit:
            print('некорректный ход, должны быть цифры, введите заново')
            insert_move = list(map(str, input('номер строки и номер '
                                              'столбца, между ними пробел:').split()))
            insert_move_str = ''.join(insert_move)
            is_digit = insert_move_str.isdigit()

    # введены две цифры
    insert_move_int = list(map(int, insert_move))

    # проверка цифр хода и повтора хода
    move_already_was = already_move(insert_move_int, player1_moves_,
                                    player2_moves_)
    if (insert_move_int[0] < 0 or insert_move_int[0] > 2
            or insert_move_int[1] < 0 or insert_move_int[1] > 2
            or move_already_was):

        while (insert_move_int[0] < 0 or insert_move_int[0] > 2
                or insert_move_int[1] < 0 or insert_move_int[1] > 2
                or move_already_was):
            print('некорректный ход, введите заново')
            insert_move = list(map(str, input('номер строки и номер '
                                              'стобца, между ними пробел:').split()))
            insert_move_int = list(map(int, insert_move))
            move_already_was = already_move(insert_move_int, player1_moves_,
                                            player2_moves_)

    correct_move = insert_move_int
    return correct_move


# функция проверяет, был ли уже такой ход, возвращает True, если ход уже был
# player_moves - все ранее сделанные игроком 1 и игроком 2 ходы
def already_move(move_made, player1_moves__, player2_moves__):
    for itter in player1_moves__:
        if move_made == itter:
            print('такой ход уже был крестиками')
            return True
    for itter in player2_moves__:
        if move_made == itter:
            print('такой ход уже был ноликами')
            return True
    return False


# функция определения победителя
def winner(symbol_of_player, m_):

    # проверяем строки на три одинаковых символа
    for row in range(0, len(m_)):
        row_sum_str = ''
        for column in range(0, len(m_[row])):
            row_sum_str += ''.join(m_[row][column])
        if row_sum_str == symbol_of_player * 3:
            return [symbol_of_player, True]

    # проверяем столбцы на три одинаковых символа
    for j__ in range(0, len(m_)):
        # генератор списка столбца j
        column_j_list = [row[j__] for row in m_]
        column_sum_str = ''
        for i_col in column_j_list:
            column_sum_str += i_col
        if column_sum_str == symbol_of_player * 3:
            return [symbol_of_player, True]

    # проверяем диагонали на три одинаковых символа

    # генератор списка значений первой диагонали квадратной матрицы
    diagonal_1 = [m_[i_diag][i_diag] for i_diag in range(0, len(m_))]
    diagonal_1_sum_str = ''
    for i_diag in diagonal_1:
        diagonal_1_sum_str += i_diag
    if diagonal_1_sum_str == symbol_of_player * 3:
        return [symbol_of_player, True]

    # генератор списка значений второй диагонали квадратной матрицы

    diagonal_2 = [m_[i_diag2][(len(m_) - 1) - i_diag2] for i_diag2 in range(0, len(m_))]
    diagonal_2_sum_str = ''
    for i_diag2 in diagonal_2:
        diagonal_2_sum_str += i_diag2
    if diagonal_2_sum_str == symbol_of_player * 3:
        return [symbol_of_player, True]

    return [symbol_of_player, False]


# игра как цикл чередования ходов, число ходов меньше или равно числу клеток
# то есть 3 * 3 = 9
# возможно играть несколько раз, результаты накапливаются

print('Игра "крестики-нолики" для двух игроков на поле 3 * 3')

player1_name = input('введите имя игрока 1: ')
player2_name = input('введите имя игрока 2: ')
player_1_result = 0
player_2_result = 0
symbol_player1 = 'x'
symbol_player2 = 'o'
print(f'{player1_name}, играете крестиками')
print(f'{player2_name}, играете ноликами')

# цикл для возможности играть несколько раз
while True:
    M = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]
    print_field(M)

    player_1 = []
    player_2 = []
    player_1_move = []
    player_2_move = []

    # цикл ходов одной игры
    for i in range(0, 9):
        print(f'ход {i+1}')

        if i % 2 == 0:  # ходят крестики
            player_1_move = move_(player1_name, player_1, player_2)
            player_1.append(player_1_move)
            M[player_1_move[0]][player_1_move[1]] = 'x'
            print_field(M)
            player1_winner = winner('x', M)

            if player1_winner[1]:
                print(f'победили крестики - {player1_name}!')
                winner_name = player1_name
                player_1_result += 1
                break

        else:  # ходят нолики
            player_2_move = move_(player2_name, player_1, player_2)
            player_2.append(player_2_move)
            M[player_2_move[0]][player_2_move[1]] = 'o'
            print_field(M)
            player2_winner = winner('o', M)

            if player2_winner[1]:
                print(f'победили нолики - {player2_name}!')
                winner_name = player2_name
                player_2_result += 1
                break

        if i == 8:
            print('все ходы сделаны, победителя нет, ничья!')

    print(f'счет по играм: {player1_name} - {player_1_result}'
          f'  {player2_name} - {player_2_result}')

    play_again = input('играем еще раз? если да - введите да ')
    if play_again != 'да':
        break

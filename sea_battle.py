"""
Игру необходимо запускать через консоль PyCharm. В командной строке сбиваются значки utf-8.
Основной файл - see_battle.py. Classes.py и enemy_field.py - вспомогательные.

На первом этапе игроку необходимо расставить собвтенные корабли на поле. Корабли расставляются путем ввода в консоль
координат поля, используя прописные латинские буквы
(A,B,C,D,E,F) для обозначения строки и цифры от 1 до 6для обозначения столбца. Координаты вводятся без пробела.

Многопалубные корабли необходимо расставлять сверху-вниз или слева-направа. Они отображаются на игровом поле после
установки 2-х палуб (третья палуба трехпалубника устанавливается
автоматически после установки первых двух палуб).

Поле соперника генерируется случайным образом.

Компьютер ходит также случайным образом, выбирая из доступных координат.
Все доступные координаты (ходы) содержатся в списках (для компьютера и игрока свой список). Использованные комбинации из
списка удаляются.

Вид игрового поля изменен, по сравнению с представленном в задании. Добавлены обозначения из стандартныхсимволов utf-8
для пустой клетки, подбитого и "живого" корабля.
Если игрок или компьютер попадают по кораблю, им предоставляется право повторного хода до промаха.

"""
import random
from enemy_field import generate_enemy_field
from classes import Ship
from classes import BattleField
from classes import check_position
import time


def check_order():
    global battleship_1
    global battleship_2

    if (battleship_2.position_row - battleship_1.position_row != 1 and
            battleship_2.position_col - battleship_1.position_col != 1):
        raise ValueError("Палубы одного корабля должны находиться рядом!")
    elif (battleship_2.position_row - battleship_1.position_row == 1 and
          battleship_2.position_col - battleship_1.position_col == 1):
        raise ValueError("Палубы одного корабля должны находиться рядом!")


bf = BattleField('Ваше поле')
# расставляем корабли

for i in range(7):

    if i == 0:
        ship_type = "трехпалубного"
        decks = 3
    elif i in range(1, 3):
        ship_type = "двуххпалубного"
        decks = 2
    else:
        ship_type = "однопалубного"
        decks = 1

    print("Расстановка кораблей: введите координаты без пробела. Последовательность расстановки палуб: сверху-вниз "
          "или слева-направо")

    if decks > 1:

        ship_set = False

        while not ship_set:
            try:
                bf.show_field()
                index_1 = input(f"Расположите первую палубу {ship_type} корабля: ")
                battleship_1 = Ship(index_1[0], index_1[1])
                check_position(battleship_1, decks, bf)
            except ValueError:
                print("Координаты введены неверно. Попробуйте еще раз.")
            else:
                try:
                    bf.show_field()
                    index_2 = input(f"Расположите вторую палубу {ship_type} корабля: ")
                    battleship_2 = Ship(index_2[0], index_2[1])
                    check_order()
                    check_position(battleship_2, decks - 1, bf)
                except ValueError:
                    print("Координаты введены неверно. Попробуйте еще раз.")
                else:
                    if decks == 3:
                        if index_1[0] == index_2[0]:
                            try:
                                bf.show_field()
                                battleship_3 = Ship(battleship_2.position_row, battleship_2.position_col + 1)
                                check_position(battleship_3, 1, bf)
                            except ValueError:
                                print("Координаты введены неверно. Попробуйте еще раз.")
                            else:
                                ship_set = True
                                bf.add_ship(battleship_1)
                                bf.add_ship(battleship_2)
                                bf.add_ship(battleship_3)
                                bf.show_field()
                        elif index_1[1] == index_2[1]:
                            try:
                                bf.show_field()
                                battleship_3 = Ship(battleship_2.position_row + 1, battleship_2.position_col)
                                check_position(battleship_3, 1, bf)
                            except ValueError:
                                print("Координаты введены неверно. Попробуйте еще раз.")
                            else:
                                ship_set = True
                                bf.add_ship(battleship_1)
                                bf.add_ship(battleship_2)
                                bf.add_ship(battleship_3)
                                bf.show_field()
                    elif decks == 2:
                        ship_set = True
                        bf.add_ship(battleship_1)
                        bf.add_ship(battleship_2)
                        bf.show_field()

    elif decks == 1:
        ship_set = False
        while not ship_set:
            try:
                bf.show_field()
                index_1 = input(f"Расположите палубу {ship_type} корабля: ")
                battleship_1 = Ship(index_1[0], index_1[1])
                check_position(battleship_1, decks, bf)
            except ValueError:
                print("Координаты введены неверно. Попробуйте еще раз.")
            else:
                bf.add_ship(battleship_1)
                ship_set = True
                bf.show_field()

print('Все корабли расставлены! Игра начинается!')
bf.show_field()
enemy_bf = BattleField()
time.sleep(3)
print("Генерируем поле соперника...")
generate_enemy_field(enemy_bf)
enemy_bf_to_show = BattleField('Поле соперника')

counter = 1
end_game = False

enemies_ships_killed = 0
players_ships_killed = 0

players_available_moves = [(i, j) for i in range(1, 7) for j in range(1, 7)]
ais_available_moves = [(i, j) for i in range(1, 7) for j in range(1, 7)]
d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
d_reverse = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}


def check_move(move_, player):
    global d
    if move_[0] in d.keys() and int(move_[1]) in range(1, 7):

        if player == "human":

            if (a_to_1(move_[0]), int(move_[1])) in players_available_moves:

                return True

            else:

                raise IndexError
        else:

            if (a_to_1(move_[0]), int(move_[1])) in ais_available_moves:

                return True

            else:

                raise IndexError

    else:
        raise ValueError


def game_over_check():
    if enemies_ships_killed == 11 or players_ships_killed == 11:
        return True


def a_to_1(move_):
    global d
    return int(d[move_])


while not end_game:
    move_made = False
    if counter % 2 == 1:
        print("Ваш ход!")

        while not move_made:

            enemy_bf_to_show.show_field()
            try:
                move = input("Введите координаты выстрела: ")
                check_move(move, 'human')
            except IndexError:
                print("Вы уже делали такой ход! Введите координаты поля, по которому вы еще не стреляли!")
            except ValueError:
                print("Вы ввели недопустимые координаты. Попробуйте еще раз!")
            else:
                row = a_to_1(move[0])
                col = int(move[1])
                if enemy_bf.hit_check(row, col):
                    enemies_ships_killed += 1
                    players_available_moves.remove((row, col))
                    enemy_bf_to_show.display_move(row, col, True)
                    if game_over_check():

                        time.sleep(1)
                        print("Вы победили! Игра окончена")
                        end_game = True
                        enemy_bf_to_show.show_field()
                        break

                    else:
                        time.sleep(1)
                        print("Попадание! Снова ваш ход!")

                else:
                    time.sleep(1)
                    print("Промах!")
                    enemy_bf_to_show.display_move(row, col)
                    players_available_moves.remove((row, col))
                    move_made = True
                    enemy_bf_to_show.show_field()
                    counter += 1

    else:
        print("Ход компьютера!")
        while not move_made:
            move = random.choice(ais_available_moves)
            row = move[0]
            col = move[1]
            time.sleep(2)
            print("Выстрел по ", d_reverse[row], col)
            if bf.hit_check(row, col):

                bf.display_move(row, col, True)
                bf.show_field()
                ais_available_moves.remove(move)
                players_ships_killed += 1

                if game_over_check():
                    time.sleep(2)
                    print("Игра окончена. Ваш флот кормит рыб")
                    bf.show_field()
                    end_game = True
                    break

                else:
                    time.sleep(2)
                    print("Попадание! Снова ход компьютера")
                    bf.show_field()
                    time.sleep(2)
            else:
                time.sleep(2)
                print("Компьютер промахивается!")
                bf.display_move(row, col)
                bf.show_field()
                time.sleep(2)
                ais_available_moves.remove(move)
                counter += 1
                move_made = True

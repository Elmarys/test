from classes import BattleField
from classes import Ship
from classes import check_position
import random


def generate_enemy_field(enemy_bf):
    field_generated = False

    while not field_generated:
        global L
        L = [(i, j) for i in range(1, 7) for j in range(1, 7)]
        enemy_bf.clean_field()
        try:
            # ставим трехпалубник

            set_trippledecker(enemy_bf)

            # ставим двухпалубники
            for i in range(2):
                set_doubledecker(enemy_bf)

            # ставим однопалубнки

            for i in range(4):
                set_singledecker(enemy_bf)

        except IndexError:
            pass
        else:
            field_generated = True


def set_trippledecker(enemy_bf):
    # ставим трехпалубник
    a = random.choice(L)
    row = a[0]
    col = a[1]
    konig_1 = Ship(row, col)
    direction = random.randint(1, 2)

    if direction == 1:
        ship_set = False
        while not ship_set:
            try:
                konig_2 = Ship(row + 1, col)
                konig_3 = Ship(row + 2, col)

            except ValueError:
                try:
                    konig_2 = Ship(row - 1, col)
                    konig_3 = Ship(row - 2, col)

                except ValueError:
                    pass
                else:
                    enemy_bf.add_ship(konig_1)
                    enemy_bf.add_ship(konig_2)
                    enemy_bf.add_ship(konig_3)
                    try:
                        delete_from_list(konig_1)
                        delete_from_list(konig_2)
                        delete_from_list(konig_3)
                    except ValueError:
                        pass
                    finally:

                        ship_set = True

            else:
                enemy_bf.add_ship(konig_1)
                enemy_bf.add_ship(konig_2)
                enemy_bf.add_ship(konig_3)
                try:
                    delete_from_list(konig_1)
                    delete_from_list(konig_2)
                    delete_from_list(konig_3)
                except ValueError:
                    pass
                finally:
                    ship_set = True

    elif direction == 2:

        ship_set = False
        while not ship_set:
            try:
                konig_2 = Ship(row, col + 1)
                konig_3 = Ship(row, col + 2)

            except ValueError:
                try:
                    konig_2 = Ship(row, col - 1)
                    konig_3 = Ship(row, col - 2)

                except ValueError:
                    pass
                else:
                    enemy_bf.add_ship(konig_1)
                    enemy_bf.add_ship(konig_2)
                    enemy_bf.add_ship(konig_3)
                    try:
                        delete_from_list(konig_1)
                        delete_from_list(konig_2)
                        delete_from_list(konig_3)
                    except ValueError:
                        pass
                    finally:
                        ship_set = True

            else:
                enemy_bf.add_ship(konig_1)
                enemy_bf.add_ship(konig_2)
                enemy_bf.add_ship(konig_3)
                try:
                    delete_from_list(konig_1)
                    delete_from_list(konig_2)
                    delete_from_list(konig_3)

                except ValueError:
                    pass
                finally:
                    ship_set = True


def set_doubledecker(enemy_bf):
    ship_set = False
    while not ship_set:
        direction = random.randint(1, 2)
        a = random.choice(L)
        row = a[0]
        col = a[1]

        if direction == 1:
            try:
                kaiser_1 = Ship(row, col)
                kaiser_2 = Ship(row + 1, col)
                check_position(kaiser_1, 2, enemy_bf)
                check_position(kaiser_2, 1, enemy_bf)
            except ValueError:
                try:
                    kaiser_1 = Ship(row, col)
                    kaiser_2 = Ship(row - 1, col)
                    check_position(kaiser_1, 2, enemy_bf)
                    check_position(kaiser_2, 1, enemy_bf)
                except ValueError:
                    pass
                else:
                    enemy_bf.add_ship(kaiser_1)
                    enemy_bf.add_ship(kaiser_2)
                    try:
                        delete_from_list(kaiser_2)
                        delete_from_list(kaiser_1)
                    except ValueError:
                        pass
                    finally:
                        ship_set = True

            else:
                enemy_bf.add_ship(kaiser_1)
                enemy_bf.add_ship(kaiser_2)
                try:
                    delete_from_list(kaiser_2)
                    delete_from_list(kaiser_1)
                except ValueError:
                    pass
                finally:
                    ship_set = True

        elif direction == 2:

            try:
                kaiser_1 = Ship(row, col)
                kaiser_2 = Ship(row, col + 1)
                check_position(kaiser_1, 2, enemy_bf)
                check_position(kaiser_2, 1, enemy_bf)
            except ValueError:
                try:
                    kaiser_1 = Ship(row, col)
                    kaiser_2 = Ship(row, col - 1)
                    check_position(kaiser_1, 2, enemy_bf)
                    check_position(kaiser_2, 1, enemy_bf)
                except ValueError:
                    pass
                else:
                    enemy_bf.add_ship(kaiser_1)
                    enemy_bf.add_ship(kaiser_2)
                    try:

                        delete_from_list(kaiser_2)
                        delete_from_list(kaiser_1)
                    except ValueError:
                        pass
                    finally:
                        ship_set = True

            else:
                enemy_bf.add_ship(kaiser_1)
                enemy_bf.add_ship(kaiser_2)
                try:
                    delete_from_list(kaiser_2)
                    delete_from_list(kaiser_1)
                except ValueError:
                    pass
                finally:
                    ship_set = True


def set_singledecker(enemy_bf):
    ship_set = False
    while not ship_set:

        a = random.choice(L)
        row = a[0]
        col = a[1]

        try:
            nassau = Ship(row, col)
            check_position(nassau, 1, enemy_bf)
        except ValueError:
            pass
        else:
            enemy_bf.add_ship(nassau)
            try:
                delete_from_list(nassau)
            except ValueError:
                pass
            finally:
                ship_set = True


def delete_from_list(ship):
    global L
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (ship.position_row + i, ship.position_col + j) in L:
                L.remove((ship.position_row + i, ship.position_col + j))

enemy_bf = BattleField()
generate_enemy_field(enemy_bf)
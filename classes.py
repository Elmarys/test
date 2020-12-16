e = "\u2B1C"  # empty field
s = "\u25A0"  # ship
d = "\u26DD"  # dead
m = "\u26AB"  # miss


class BattleField:

    def __init__(self, whose_field=None, field=None):
        if field is None:
            field = [[' ', '1', ' 2', '3', '4', ' 5', '6'],
                     ['A', e, e, e, e, e, e],
                     ['B', e, e, e, e, e, e],
                     ['C', e, e, e, e, e, e],
                     ['D', e, e, e, e, e, e],
                     ['E', e, e, e, e, e, e],
                     ['F', e, e, e, e, e, e]]
        self.field = field
        self.whose_field = whose_field

    def show_field(self):
        print(self.whose_field)
        for cell in self.field:
            print(' '.join(cell))

    def clean_field(self):
        for i in range(1, 7):
            for j in range(1, 7):
                self.field[i][j] = e

    def add_ship(self, ship):
        if self.is_empty_position(ship):
            self.field[ship.position_row][ship.position_col] = s
            return True
        else:
            print("Здесь уже стоит корабль! Введите другие координаты")

    def hit_check(self, row, col):
        if self.field[row][col] == s:
            self.field[row][col] = d
            return True
        else:
            self.field[row][col] = m
            return False

    def display_move(self, row, col, hit=False):
        if hit:
            self.field[row][col] = d
        else:
            self.field[row][col] = m

    def is_empty_position(self, ship):
        if self.field[ship.position_row][ship.position_col] != s:
            return True

    def is_empty_position2(self, row, col):

        flag = True
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                try:
                    if self.field[r][c] == s:
                        flag = False
                except IndexError:
                    pass
        return flag


class Ship:
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

    def __init__(self, row, col):
        self.position_row = row
        self.position_col = col

    @property
    def position_row(self):
        if self.__row in self.d.keys():
            return self.a_to_1(self.__row)
        else:
            return int(self.__row)

    @property
    def position_col(self):
        return int(self.__col)

    def a_to_1(self, row):
        return int(self.d[row])

    @position_row.setter
    def position_row(self, row):
        if row not in self.d.keys():

            if not int(row) in range(1, 7):
                raise ValueError("Position is out of the field")
        self.__row = row

    @position_col.setter
    def position_col(self, col):
        if not int(col) in range(1, 7):
            raise ValueError("Position is out of the field")
        self.__col = int(col)


def check_position(battleship, decks, battlefield):
    if not battlefield.is_empty_position2(battleship.position_row, battleship.position_col):
        raise ValueError("Здесь нельзя размещать корабль!")

    if decks == 3:
        if (battlefield.is_empty_position2(battleship.position_row + 1, battleship.position_col) and
                battlefield.is_empty_position2(battleship.position_row + 2, battleship.position_col) and
                battlefield.is_empty_position2(battleship.position_row + 3, battleship.position_col)):

            return True

        elif (battlefield.is_empty_position2(battleship.position_row, battleship.position_col + 1) and
              battlefield.is_empty_position2(battleship.position_row, battleship.position_col + 2) and
              battlefield.is_empty_position2(battleship.position_row, battleship.position_col + 3)):

            return True

        else:
            raise ValueError("Здесь нельзя размещать корабль!")

    if decks == 2:

        if (battlefield.is_empty_position2(battleship.position_row + 1, battleship.position_col) and
                battlefield.is_empty_position2(battleship.position_row + 2, battleship.position_col)):

            return True

        elif (battlefield.is_empty_position2(battleship.position_row, battleship.position_col + 1) and
              battlefield.is_empty_position2(battleship.position_row, battleship.position_col + 2)):

            return True

        else:
            raise ValueError("Здесь нельзя размещать корабль!")

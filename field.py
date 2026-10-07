from koma import Koma

class Field:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

        self.board[3][3] = Koma(3, 3, "W")
        self.board[3][4] = Koma(4, 3, "B")
        self.board[4][3] = Koma(3, 4, "B")
        self.board[4][4] = Koma(4, 4, "W")

    def put_koma(self, x, y, state):
        self.board[y][x] = Koma(x, y, state)

    def reverse_koma(self, x, y):
        koma = self.board[y][x]

        if koma is not None:
            koma.change_state()

    def reverse_right(self, x, y, state):
        for i in range(x + 1, 8):
            koma = self.board[y][i]

            if koma is None:
                break

            if koma.state == state:
                for j in range(x + 1, i):
                    self.board[y][j].change_state()
                break

    def reverse_left(self, x, y, state):
        for i in range(x - 1, -1, -1):
            koma = self.board[y][i]

            if koma is None:
                break

            if koma.state == state:
                for j in range(x - 1, i, -1):
                    self.board[y][j].change_state()
                break

    def reverse_up(self, x, y, state):
        for i in range(y - 1, -1, -1):
            koma = self.board[i][x]

            if koma is None:
                break

            if koma.state == state:
                for j in range(y - 1, i, -1):
                    self.board[j][x].change_state()
                break

    def reverse_down(self, x, y, state):
        for i in range(y + 1, 8):
            koma = self.board[i][x]

            if koma is None:
                break

            if koma.state == state:
                for j in range(y + 1, i):
                    self.board[j][x].change_state()
                break

    def reverse_up_right(self, x, y, state):
        i = x + 1
        j = y - 1

        while i < 8 and j >= 0:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k = x + 1
                l = y - 1

                while k < i and l > j:
                    self.board[l][k].change_state()
                    k += 1
                    l -= 1

                break

            i += 1
            j -= 1

    def reverse_up_left(self, x, y, state):
        i = x - 1
        j = y - 1

        while i >= 0 and j >= 0:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k = x - 1
                l = y - 1

                while k > i and l > j:
                    self.board[l][k].change_state()
                    k -= 1
                    l -= 1

                break

            i -= 1
            j -= 1

    def reverse_down_right(self, x, y, state):
        i = x + 1
        j = y + 1

        while i < 8 and j < 8:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k = x + 1
                l = y + 1

                while k < i and l < j:
                    self.board[l][k].change_state()
                    k += 1
                    l += 1

                break

            i += 1
            j += 1

    def reverse_down_left(self, x, y, state):
        i = x - 1
        j = y + 1

        while i >= 0 and j < 8:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k = x - 1
                l = y + 1

                while k > i and l < j:
                    self.board[l][k].change_state()
                    k -= 1
                    l += 1

                break

            i -= 1
            j += 1
    def reverse_all(self, x, y, state):
        self.reverse_right(x, y, state)
        self.reverse_left(x, y, state)
        self.reverse_up(x, y, state)
        self.reverse_down(x, y, state)
        self.reverse_up_right(x, y, state)
        self.reverse_up_left(x, y, state)
        self.reverse_down_right(x, y, state)
        self.reverse_down_left(x, y, state)


field = Field()

field.put_koma(4, 5, "B")
field.reverse_all(4, 5, "B")

for row in field.board:
    for koma in row:
        if koma is None:
            print(".", end=" ")
        else:
            print(koma.state, end=" ")
    print()
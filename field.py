

from koma import Koma


class Field:
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]

        self.board[3][3] = Koma(3, 3, "W")
        self.board[3][4] = Koma(4, 3, "B")
        self.board[4][3] = Koma(3, 4, "B")
        self.board[4][4] = Koma(4, 4, "W")

    def display(self):
        for row in self.board:
            print(" ".join(
                koma.state if koma else "."
                for koma in row
            ))

    def can_put_koma(self, x, y, state):
        if not (0 <= x < 8 and 0 <= y < 8):
            return False

        if self.board[y][x] is not None:
            return False

        directions = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1),  (1, 1)
        ]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            found_opponent = False

            while 0 <= nx < 8 and 0 <= ny < 8:
                koma = self.board[ny][nx]

                if koma is None:
                    break

                if koma.state != state:
                    found_opponent = True
                else:
                    if found_opponent:
                        return True
                    break

                nx += dx
                ny += dy

        return False

    def put_koma(self, x, y, state):
        if not self.can_put_koma(x, y, state):
            return False

        self.board[y][x] = Koma(x, y, state)

        directions = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1),  (1, 1)
        ]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            to_flip = []

            while 0 <= nx < 8 and 0 <= ny < 8:
                koma = self.board[ny][nx]

                if koma is None:
                    break

                if koma.state != state:
                    to_flip.append(koma)
                else:
                    for opponent in to_flip:
                        opponent.change_state()
                    break

                nx += dx
                ny += dy

        return True

    def get_valid_moves(self, state):
        moves = []

        for y in range(8):
            for x in range(8):
                if self.can_put_koma(x, y, state):
                    moves.append((x, y))

        return moves

    def has_valid_move(self, state):
        return len(self.get_valid_moves(state)) > 0

    def count_stones(self, state):
        count = 0

        for row in self.board:
            for koma in row:
                if koma is not None and koma.state == state:
                    count += 1

        return count


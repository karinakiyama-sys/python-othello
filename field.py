
from koma import Koma


class Field:
    def __init__(self):
        # 8×8の盤面を作る
        self.board = [[None for _ in range(8)] for _ in range(8)]

        # 初期配置
        self.board[3][3] = Koma(3, 3, "W")
        self.board[3][4] = Koma(4, 3, "B")
        self.board[4][3] = Koma(3, 4, "B")
        self.board[4][4] = Koma(4, 4, "W")

    # 石を置けるか判定する
    def can_put_koma(self, x, y, state):
        # 盤面の範囲外なら置けない
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return False

        # すでに石がある場所には置けない
        if self.board[y][x] is not None:
            return False

        # 8方向（横・縦・斜め）
        directions = [
            (1, 0), (-1, 0),
            (0, -1), (0, 1),
            (1, -1), (-1, -1),
            (1, 1), (-1, 1)
        ]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 隣が盤面内で、相手の石か確認
            if not (0 <= nx < 8 and 0 <= ny < 8):
                continue

            koma = self.board[ny][nx]

            if koma is None or koma.state == state:
                continue

            # 相手の石が続く間、同じ方向に進む
            while 0 <= nx < 8 and 0 <= ny < 8:
                koma = self.board[ny][nx]

                if koma is None:
                    break

                if koma.state == state:
                    # 自分の石で挟めた
                    return True

                nx += dx
                ny += dy

        return False

    # 石を置く
    def put_koma(self, x, y, state):
        if not self.can_put_koma(x, y, state):
            return False

        self.board[y][x] = Koma(x, y, state)
        self.reverse_all(x, y, state)

        return True

    # 指定した石の色を反転する
    def reverse_koma(self, x, y):
        koma = self.board[y][x]

        if koma is not None:
            koma.change_state()

    # 右方向
    def reverse_right(self, x, y, state):
        for i in range(x + 1, 8):
            koma = self.board[y][i]

            if koma is None:
                break

            if koma.state == state:
                for j in range(x + 1, i):
                    self.reverse_koma(j, y)
                break

    # 左方向
    def reverse_left(self, x, y, state):
        for i in range(x - 1, -1, -1):
            koma = self.board[y][i]

            if koma is None:
                break

            if koma.state == state:
                for j in range(x - 1, i, -1):
                    self.reverse_koma(j, y)
                break

    # 上方向
    def reverse_up(self, x, y, state):
        for i in range(y - 1, -1, -1):
            koma = self.board[i][x]

            if koma is None:
                break

            if koma.state == state:
                for j in range(y - 1, i, -1):
                    self.reverse_koma(x, j)
                break

    # 下方向
    def reverse_down(self, x, y, state):
        for i in range(y + 1, 8):
            koma = self.board[i][x]

            if koma is None:
                break

            if koma.state == state:
                for j in range(y + 1, i):
                    self.reverse_koma(x, j)
                break

    # 右上方向
    def reverse_up_right(self, x, y, state):
        i, j = x + 1, y - 1

        while i < 8 and j >= 0:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k, l = x + 1, y - 1

                while k < i and l > j:
                    self.reverse_koma(k, l)
                    k += 1
                    l -= 1

                break

            i += 1
            j -= 1

    # 左上方向
    def reverse_up_left(self, x, y, state):
        i, j = x - 1, y - 1

        while i >= 0 and j >= 0:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k, l = x - 1, y - 1

                while k > i and l > j:
                    self.reverse_koma(k, l)
                    k -= 1
                    l -= 1

                break

            i -= 1
            j -= 1

    # 右下方向
    def reverse_down_right(self, x, y, state):
        i, j = x + 1, y + 1

        while i < 8 and j < 8:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k, l = x + 1, y + 1

                while k < i and l < j:
                    self.reverse_koma(k, l)
                    k += 1
                    l += 1

                break

            i += 1
            j += 1

    # 左下方向
    def reverse_down_left(self, x, y, state):
        i, j = x - 1, y + 1

        while i >= 0 and j < 8:
            koma = self.board[j][i]

            if koma is None:
                break

            if koma.state == state:
                k, l = x - 1, y + 1

                while k > i and l < j:
                    self.reverse_koma(k, l)
                    k -= 1
                    l += 1

                break

            i -= 1
            j += 1

    # 8方向すべての石を反転する
    def reverse_all(self, x, y, state):
        self.reverse_right(x, y, state)
        self.reverse_left(x, y, state)
        self.reverse_up(x, y, state)
        self.reverse_down(x, y, state)
        self.reverse_up_right(x, y, state)
        self.reverse_up_left(x, y, state)
        self.reverse_down_right(x, y, state)
        self.reverse_down_left(x, y, state)
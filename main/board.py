import random

from main import Tiles


class Board(object):
    def __init__(self) -> None:
        self.board = [[Tiles() for _ in range(4)] for _ in range(4)]

    def get_tiles(self, x: int, y: int) -> Tiles:
        return self.board[x][y]

    def get_value(self, x: int, y: int) -> int:
        return self.get_tiles(x, y).value

    def empty_tiles(self) -> list:
        results = []
        for i in range(4):
            for j in range(4):
                results.append((i, j)) if not self.get_value(i, j) else None
        return results

    def set_random(self) -> None:
        self.get_tiles(random.choice(self.empty_tiles())).set_value(random.choice(2, 4))

    def neighbors(self, x: int, y: int) -> list:
        result = []
        result.append((x - 1, y)) if x > 0 else None
        result.append((x, y - 1)) if y > 0 else None
        result.append((x + 1, y)) if x < 3 else None
        result.append((x, y + 1)) if y < 3 else None

        return result

    def check_neighbor(self, x: int, y: int) -> bool:
        return any(
            [
                self.get_value(x, y) == self.get_value(nx, ny)
                for nx, ny in self.neighbors()
            ]
        )

    def game_over(self) -> bool:
        if not self.empty_tiles():
            for i in range(4):
                for j in range(4):
                    if self.check_neighbor(i, j):
                        return True
        return False

    def compress(self) -> None:
        new_tmp_board = [[Tiles() for _ in range(4)] for _ in range(4)]

        for i in range(4):
            pos = 0
            for j in range(4):
                if self.get_value(i, j):
                    new_tmp_board[i][pos] = self.get_tiles(i, j)
                    pos += 1

        self.board = new_tmp_board

    def merge(self) -> None:
        for i in range(4):
            for j in range(3):
                if self.get_value(i, j) and (
                    self.get_value(i, j) == self.get_value(i, j + 1)
                ):
                    self.get_tiles(i, j).double()
                    self.get_tiles(i, j + 1).empty()

    def reverse(self) -> None:
        self.board = [row.reverse() for row in self.board]

    def transpose(self) -> None:
        self.board = [list(i) for i in zip(*self.board)]

    def move(self) -> None:
        self.compress()
        self.merge()

    def __str__(self) -> str:
        s = [[str(e) for e in row] for row in self.board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = "\t".join("{{:{}}}".format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return "\n".join(table)

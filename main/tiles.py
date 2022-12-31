class Tiles(object):
    def __init__(self) -> None:
        self.value = None

    def empty(self) -> None:
        self.value = None

    def set_value(self, value: int) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

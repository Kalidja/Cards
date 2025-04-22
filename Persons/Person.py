from typing import Callable
from Hand import Hand


class Person:
    def __init__(self, name: str, status) -> None:
        self.name = name
        self.status: str = status
        self.hand: Hand = Hand()

    def move(self, move = Callable[..., None]) -> None:
        move()
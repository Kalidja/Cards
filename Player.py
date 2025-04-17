from typing import Callable, List
from Deck import Deck, Deck52
from Card import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.number = 0
        self.hand: List[Card] = []

    def move(self, move = Callable[..., None]) -> None:
        move()
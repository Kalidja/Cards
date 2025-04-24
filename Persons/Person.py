from typing import Callable, Union, Iterable
from Card import Card
from Hand import Hand


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: Union[Hand, Iterable[Card]] = Hand()

    def draw_card(self, card: Card) -> None:
        self.hand.append(card)

    def play_first_card(self) -> None:
        if self.hand:
            return self.hand.pop(0)
        return None

    def play_card(self, index: int) -> None:
        if self.hand:
            return self.hand.pop(index)
        return None

    def __repr__(self) -> str:
        return f"Person(name={self.name}, hand={self.hand})"
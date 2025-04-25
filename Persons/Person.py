from typing import Optional, Union, Iterable
from Card import Card
from Hand import Hand


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: Union[Hand, Iterable[Card]] = Hand()

    def draw_card(self, card: Card) -> None:
        self.hand.append(card)

    def play_first_card(self) -> Optional[Card]:
        try:
            return self.hand.pop(0)
        except IndexError:
            raise IndexError

    def play_card(self, index: int) -> None:
        if self.hand:
            return self.hand.pop(index)
        return None

    def __repr__(self) -> str:
        return f"Person(name={self.name}, {len(self.hand)} hand={self.hand})"
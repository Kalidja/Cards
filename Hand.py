from typing import Iterable, Optional
from  Card import Card

class Hand(list):
    def __init__(self, card_list: Optional[Iterable[Card]] = None) -> None:
        if card_list is None:
            super().__init__()
        else:
            for card in card_list:
                if not isinstance(card, Card):
                    raise TypeError(f"{card} is not a Card.")
            super().__init__(card_list)


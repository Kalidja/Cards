from typing import Iterable, Callable, Optional, List
from Card import Card

class Deck:
    def __init__(self, cards: Optional[Iterable[Card]] = None):
        if cards:
            self.deck = list(cards)
            self.order = list(cards)
        else:
            self.deck = []
            self.order = []

    def shuffle(self, key: Optional[Callable[[List[Card]], List[Card]]] = None):
        if key:
            self.order = key(self.order)


    def make_32_card_deck(self):
        if not self.deck:
            card_list =


    def make_54_card_deck(self):
        if not self.deck:
            pass


    def make_56_card_deck(self):
        if not self.deck:
            pass




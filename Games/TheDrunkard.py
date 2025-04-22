from Card import Card
from Deck import Deck, Deck52
from typing import List, Optional, Dict
from Persons.Person import Person
from Persons.Dealer import Dealer
from Games.Game import Game
from Settings.Lists import dealer_names
from random import randint


class TheDrunkard(Game):
    def __init__(self, deck: Deck) -> None:
        super().__init__(4, deck, True, Dealer(dealer_names[randint(0, len(dealer_names) - 1)]))
        self.cards_in_game: List[Card] = []

    def split_deck(self) -> None:
        while self.deck.order:
            for i in self.players:
                i.hand.append(self.deck.order.pop(0))

    def next_turn(self) -> None:
        pass
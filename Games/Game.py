from Deck import Deck
from Card import Card
from typing import List, Callable, Optional, Dict, Union
from Persons.Dealer import Dealer
from Persons.Person import Person
from Persons.Player import Player


class Game:
    def __init__(self, max_players: int, deck: Deck, even_number_of_players: bool, dealer: Optional[Dealer] = None) -> None:
        self.dealer = dealer
        self.max_count_players = max_players
        self.even_number_of_players = even_number_of_players
        self.deck = deck
        self.players: List[Player] = []
        self.dealer = dealer

    def set_players(self, players: List[Player]) -> None:
        self.players = players

    def shuffle_deck(self, funk: Callable[[List[Card]], List[Card]]) -> None:
        self.deck.shuffle(funk)

    def split_deck(self) -> Dict["Person", "Deck"]:
        pass

    def next_turn(self) -> None:
        pass

    def player_move(self) -> None:
        pass

    def dealer_move(self) -> None:
        pass

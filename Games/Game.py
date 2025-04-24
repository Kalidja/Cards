from Deck import Deck
from Card import Card
from typing import List, Callable, Optional, Dict, Union
from Persons.Dealer import Dealer
from Persons.Person import Person
from Persons.Player import Player
from Logger import Logger


class Game:
    def __init__(self, max_players: int, deck: Deck, dealer: Optional[Dealer] = None) -> None:
        self.deck = deck
        self.max_players = max_players
        if dealer:
            self.dealer = dealer
        self._players: List[Player] = []
        self.discards: List[Card] = []
        self.cards_in_game: Dict[Person, List[Card]] = {}
        self.logger: Logger = Logger(self.__class__.__name__)

    def set_players(self, players: List[Player]) -> None:
            self._players = players

    def split_deck(self) -> None:
        pass

    def new_turn(self) -> None:
        pass

    def start_game(self) -> None:
        pass

    def end_game(self) -> None:
        pass

    def check_turn_winner(self) -> None:
        pass

    def check_winner(self) -> None:
        pass

    def eliminate_looser(self, player: Player) -> None:
        if self._players:
            self._players.remove(player)
        else:
            raise Exception("No players left.")


from Deck import Deck, Deck52
from typing import List
from Player import Player
from Deck import Deck


class Game:
    def __init__(self, players = List[Player], deck = Deck) -> None:
        self.players = players
        self.deck = deck
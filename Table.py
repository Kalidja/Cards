from typing import Iterable, Optional, List
from Persons.Player import Player
from Persons.Dealer import Dealer
from Games.Game import Game

class Table:
    def __init__(self, table_number: int, game: Game) -> None:
        self.game = game
        self.table_number = table_number
        self._parce_game_settings()
        self.players: List[Player] = []
        self.table_is_full: bool = False
        self.game_is_started = False

    def _parce_game_settings(self) -> None:
        if self.game.dealer:
            self.dealer = self.game.dealer
        self.deck = self.game.deck

    def add_new_player(self, player: Player) -> None:
        if self.game_is_started:
            raise ValueError(f"Game already started")
        if not self.table_is_full:
            self.players.append(player)
            if len(self.players) == self.game.max_players:
                self.table_is_full = True
        else:
            raise ValueError(f"Table number {self.table_number} is full")

    def remove_player(self, player: Player) -> None:
        if self.game_is_started:
            raise ValueError(f"Game already started")
        try:
            self.players.remove(player)
        except ValueError as e:
            print(f"The player {player.name} is not in the table")

    def start_game(self) -> None:
        if self.game_is_started:
            raise ValueError(f"Game already started")
        else:
            self.game_is_started = True
            self.game.set_players(self.players)
            self.game.start_game()


import sys
from Card import Card
from Deck import Deck, Deck32, CustomDeck
from typing import List, Optional, Dict, Union, Tuple, Type
from Persons.Person import Person
from Games.Game import Game
from Persons.Player import Player
from Shuffle import Shuffle
from random import shuffle
import Visualizer


class TheDrunkard(Game):
    def __init__(self, deck: Deck) -> None:
        super().__init__(4, deck)
        self._temp_deck_from_elem_players: List[Card] = []
        self.turns: int = 0

    def start_game(self) -> None:
        self.logger.open_logger()
        self.logger.log("Starting game...")
        if not self._players:
            raise ValueError("TheDrunkard has no players")
        if not self.deck.deck:
            raise ValueError("TheDrunkard has no deck")
        for player in self._players:
            self.cards_in_game[player] = []
        self.deck.shuffle(Shuffle.swing_card)
        shuffle(self.deck.deck)
        self.logger.log("Deck shuffled...")
        self.split_deck()
        self.logger.log("Deck split...")
        while self.new_turn():
            pass
        self.logger.log(f"Game Winner is {self._players[0].name}")
        self.end_game()

    def split_deck(self) -> None:
        while self.deck.deck:
            for i in self._players:
                i.hand.append(self.deck.deck.pop(0))

    def new_turn(self) -> bool:
        self.turns += 1
        self.logger.log("Turn #{}".format(self.turns), empty_row = True)
        if self.turns > 1000:
            self.logger.log("Infinity loop")
            self.logger.log("Game Over")
            sys.exit()
        for i in self.cards_in_game:
            self.cards_in_game[i].clear()

        if self._temp_deck_from_elem_players:
            self._temp_deck_from_elem_players.clear()

        for i in self._players:
            self.logger.log(repr(i))
            self.cards_in_game[i].append(i.play_first_card())

        Visualizer.visualize(self.cards_in_game)
        drinkers = self.check_drunk()
        while drinkers:
            drinkers = self.drunk(drinkers)
        p = self.check_turn_winner()
        self.logger.log("Winner on turn #{0} is {1}".format(self.turns, p.name))
        self.from_table_to_player(p)

        self.logger.log(f"At the end of Turn #{self.turns}, players hands:")
        for i in self._players:
            self.logger.log(f"{i.name}: {i.hand}", level=1)
        self.check_players_without_cards()
        return self.check_winner()


    def check_drunk(self) -> Union[List[Tuple[Person, Person]], None]:
        try:
            single_cards: Dict[Type, Person] = {}
            pairs: List[Tuple[Person, Person]] = []
            max_cards = max([len(x) for x in self.cards_in_game.values()])
            self.logger.log("Check drunk...")
            self.logger.log(f"Players hands:")
            for i in self.cards_in_game:
                self.logger.log(repr(i), level=1)
            self.logger.log(f"Cards in game:")
            for i in self.cards_in_game:
                self.logger.log(repr(self.cards_in_game[i]), level=1)
            for i, v in self.cards_in_game.items():
                if len(v) < max_cards:
                    continue
                last_card_type = type(v[-1].value)
                if last_card_type in single_cards:
                    if not pairs:
                        pairs.append((single_cards[last_card_type], i))
                    else:
                        for j, v in enumerate(pairs):
                            if v[0] == single_cards[last_card_type]:
                                pairs[j] = (*[x for x in v if x != i], i)
                            else:
                                pairs.append((single_cards[last_card_type], i))
                else:
                    single_cards[last_card_type] = i
            self.logger.log("No drinking players..." if not pairs else pairs)
            return pairs if pairs else None
        except ValueError as e:
            self.logger.log(f"All players run out of cards: DRAW")
            sys.exit()

    def drunk(self, drinkers: List[Tuple[Person, Person]]) -> List[Tuple[Person, Person]]:
        self.logger.log(f"Drinking persons: {drinkers}")
        for i in drinkers:
            for j in i:
                try:
                    self.cards_in_game[j].append(j.play_first_card())
                    self.cards_in_game[j].append(j.play_first_card())
                except IndexError:
                    self.logger.log(f"Player {j.name} is run out of cards")
                    self._temp_deck_from_elem_players.extend(self.cards_in_game[j])
                    self.eliminate_looser(j)
                    self.cards_in_game.pop(j)
                    continue
        return self.check_drunk()

    def check_turn_winner(self) -> Union[Person, None]:
        self.logger.log(f"Checking turn winner: {self.turns}")
        max_len = len(max(self.cards_in_game.values(), key= lambda x: len(x)))
        last_played_cards = [type(cards[-1].value) for cards in self.cards_in_game.values() if cards and len(cards) == max_len]
        if self.deck.min_card in last_played_cards and self.deck.max_card in last_played_cards:
            return min(filter(lambda x: len(x[1]) == max_len, self.cards_in_game.items()), key=lambda x: x[1][-1].value.value)[0]
        return max(filter(lambda x: len(x[1]) == max_len, self.cards_in_game.items()), key=lambda x: x[1][-1].value.value)[0]

    def from_table_to_player(self, player: Person) -> None:
        for i in self._players:
            if i == player:
                for j in self.cards_in_game.keys():
                    i.hand.extend(self.cards_in_game[j])
                i.hand.extend(self._temp_deck_from_elem_players)

    def check_winner(self) -> bool:
        return False if len(self._players) == 1 else True

    def check_players_without_cards(self) -> None:
        for i in self._players:
            if not i.hand:
                self.eliminate_looser(i)
                self.logger.log("Player {} has no cards".format(i.name))
                self.cards_in_game.pop(i)

    def end_game(self) -> None:
        self.logger.log("Game ended...")
        self.logger.close_logger()


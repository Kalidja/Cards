from Card import Card
from Deck import Deck, Deck52
from typing import List, Optional, Dict, Union, Tuple
from Persons.Person import Person
from Persons.Dealer import Dealer
from CardValue import CardValue
from Games.Game import Game
from Persons.Player import Player
from Shuffle import Shuffle
from random import shuffle


class TheDrunkard(Game):
    def __init__(self, deck: Deck) -> None:
        super().__init__(4, deck)

    def start_game(self) -> None:
        if not self._players:
            raise ValueError("TheDrunkard has no players")
        if not self.deck.deck:
            raise ValueError("TheDrunkard has no deck")
        for player in self._players:
            self.cards_in_game[player] = []
        self.deck.shuffle(Shuffle.swing_card)
        shuffle(self.deck.deck)
        self.split_deck()
        self.new_turn()

    def split_deck(self) -> None:
        while self.deck.deck:
            for i in self._players:
                i.hand.append(self.deck.deck.pop(0))

    def new_turn(self) -> None:
        for i in self._players:
            self.cards_in_game[i].append(i.hand.pop(0))
        self.check_drunk()

    def check_drunk(self) -> Union[List[Player], None]:
        index_map: Dict[CardValue, Person] = {}
        pairs: List[Tuple[Person, Person]] = []
        for p, v in self.cards_in_game.items():
            if v[-1] in index_map.values():
                pairs.append((p, index_map[v[-1].value]))
            else:
                index_map[v[-1].value] = p
        return


    def drunk(self):
        pass




deck = Deck52()
p1 = Player("p1")
p2 = Player("p2")
p3 = Player("p1")
p4 = Player("p2")
game = TheDrunkard(deck)
game.set_players([p1, p2, p3, p4])
game.start_game()
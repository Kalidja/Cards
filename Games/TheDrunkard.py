from Card import Card
from Deck import Deck, Deck32, CustomDeck
from typing import List, Optional, Dict, Union, Tuple, Type
from Persons.Person import Person
from Games.Game import Game
from Persons.Player import Player
from Shuffle import Shuffle
from random import shuffle
from CardValue import Six, Seven, Eight


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
        self.check_players_without_cards()
        self.turns += 1
        self.logger.log("Turn #{}".format(self.turns))

        for i in self.cards_in_game:
            self.cards_in_game[i].clear()

        if self._temp_deck_from_elem_players:
            self._temp_deck_from_elem_players.clear()

        for i in self._players:
            self.cards_in_game[i].append(i.hand.pop(0))

        drinkers = self.check_drunk()
        while drinkers:
            drinkers = self.drunk(drinkers)
        p = self.check_turn_winner()
        self.logger.log("Winner on turn #{0} is {1}".format(self.turns, p.name))
        self.from_table_to_player(p)
        print(p.hand)
        return self.check_winner()


    def check_drunk(self) -> Union[List[Tuple[Person, Person]], None]:
        max_cards = max([len(x) for x in self.cards_in_game.values()])
        single_cards: Dict[Type, Person] = {}
        pairs: List[Tuple[Person, Person]] = []

        self.logger.log("Check drunk...")
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

    def drunk(self, drinkers: List[Tuple[Person, Person]]) -> List[Tuple[Person, Person]]:
        for i in drinkers:
            for j in i:
                try:
                    self.cards_in_game[j].append(j.hand.pop(0))
                    self.cards_in_game[j].append(j.hand.pop(0))
                except IndexError:
                    print(f"У игрока {j.name} закончились карты. Пропускаем.")
                    self._temp_deck_from_elem_players.extend(self.cards_in_game[j])
                    self.eliminate_looser(j)
                    self.cards_in_game.pop(j)
                    continue
        return self.check_drunk()


    def check_turn_winner(self) -> Union[Person, None]:
        return max(self.cards_in_game.items(), key=lambda x: x[1][-1].value.value)[0]

    def from_table_to_player(self, player: Person) -> None:
        for i in self._players:
            if i == player:
                for j in self.cards_in_game.keys():
                    i.hand = self.cards_in_game[j] + i.hand
                i.hand = self._temp_deck_from_elem_players + i.hand

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

Cards = [Card(Six(0)), Card(Six(0)), Card(Six(0)), Card(Seven(1))]

deck = Deck32()
p1 = Player("p1")
p2 = Player("p2")
p3 = Player("p3")
p4 = Player("p4")
game = TheDrunkard(deck)
game.set_players([p1, p2, p3, p4])
game.start_game()
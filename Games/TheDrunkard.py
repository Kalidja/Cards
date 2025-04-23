from Card import Card
from Deck import Deck, Deck52, CustomDeck
from typing import List, Optional, Dict, Union, Tuple, Type
from Persons.Person import Person
from Persons.Dealer import Dealer
from CardValue import CardValue
from Games.Game import Game
from Persons.Player import Player
from Shuffle import Shuffle
from random import shuffle

from CardValue import Six, Seven, Eight


class TheDrunkard(Game):
    def __init__(self, deck: Deck) -> None:
        super().__init__(4, deck)
        self._temp_deck_for_elem_players: List[Card] = []

    def start_game(self) -> None:
        if not self._players:
            raise ValueError("TheDrunkard has no players")
        if not self.deck.deck:
            raise ValueError("TheDrunkard has no deck")
        for player in self._players:
            self.cards_in_game[player] = []
        #self.deck.shuffle(Shuffle.swing_card)
        #shuffle(self.deck.deck)
        self.split_deck()
        self.new_turn()

    def split_deck(self) -> None:
        while self.deck.deck:
            for i in self._players:
                i.hand.append(self.deck.deck.pop(0))

    def new_turn(self) -> None:
        for i in self._players:
            self.cards_in_game[i].append(i.hand.pop(0))
        drinkers = self.check_drunk()

        while drinkers:
            for i in drinkers:
                for j in i:
                    try:
                        # Попытка вытащить карту из руки и добавить её в игру
                        self.cards_in_game[j].append(j.hand.pop(0))
                    except IndexError:
                        # Обработка ситуации, если в руке больше нет карт
                        print(f"У игрока {j.name} закончились карты. Пропускаем.")
                        self._temp_deck_for_elem_players.extend(self.cards_in_game[j])
                        self._players.remove(j)
                        self.cards_in_game.pop(j)
                        continue  # Продолжаем цикл для следующего игрока
                # Обновление списка "пьяных" игроков после каждой итерации
                drinkers = self.check_drunk()

        pass




    def check_drunk(self) -> Union[List[Tuple[Person, Person]], None]:
        max_cards = max([len(x) for x in self.cards_in_game.values()])
        single_cards: Dict[Type, Person] = {}
        pairs: List[Tuple[Person, Person]] = []

        for i, v in self.cards_in_game.items():
            if len(v) < max_cards:
                pass
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

        return pairs if pairs else None



    def drunk(self):
        pass




Cards = [Card(Six(0)), Card(Six(0)), Card(Six(0)), Card(Seven(1))]

deck = CustomDeck(Cards)
p1 = Player("p1")
p2 = Player("p2")
p3 = Player("p3")
p4 = Player("p4")
game = TheDrunkard(deck)
game.set_players([p1, p2, p3, p4])
game.start_game()
from typing import Iterable, Callable, Optional, List
from Card import Card, Heart, Spade, Diamond, Club
from CardValue import CardValue, Ace, King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two
import Shuffle


suit_list = [Diamond, Club, Heart, Spade]
card_list = [Ace, King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two]


class Deck:
    def __init__(self, cards: Optional[Iterable[Card]] = None) -> None:
        if cards:
            self.deck = list(cards)
            self.order = list(cards)
        else:
            self.deck = []
            self.order = []
            self._make_deck()

    def shuffle(self, key: Optional[Callable[[List[Card]], List[Card]]] = None) -> None:
        if key:
            self.order = key(self.order)

    def _make_deck(self) -> None:
        pass

    def _make_whole_suit(self, value: CardValue) -> List[Card]:
        return_list = []
        for i in suit_list:
            return_list.append(i(value()))
        return return_list


class Deck32(Deck):
    def _make_deck(self) -> None:
        if not self.deck:
            for i in card_list[:9]:
                self.deck.extend(self._make_whole_suit(i))
                self.order.extend(self._make_whole_suit(i))


class Deck52(Deck):
    def _make_deck(self) -> None:
        if not self.deck:
            for i in card_list:
                self.deck.extend(self._make_whole_suit(i))
                self.order.extend(self._make_whole_suit(i))


class CustomDeck(Deck):
    def __init__(self, cards: Iterable[Card]) -> None:
        super().__init__(cards)
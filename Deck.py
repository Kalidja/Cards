from typing import Iterable, Callable, Optional, List, Tuple, Type, Dict
from Card import Card, Heart, Spade, Diamond, Club
from CardValue import CardValue, Ace, King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two


suit_list = [Diamond, Club, Heart, Spade]
card_list = [(Ace, 12), (King, 11), (Queen, 10), (Jack, 9), (Ten, 8), (Nine, 7), (Eight, 6), (Seven, 5), (Six, 4), (Five, 3), (Four, 2), (Three, 1), (Two, 0)]


class Deck:
    def __init__(self, cards: Optional[Iterable[Card]] = None,) -> None:
        self.cards_value: Dict[Type[CardValue], int] = {}
        if cards:
            self.deck = list(cards)
            self._set_card_value_dict()
        else:
            self.deck = []
            self._make_deck()
            self._set_card_value_dict()

    def shuffle(self, func: Optional[Callable[[List[Card]], List[Card]]] = None) -> None:
        if func:
            self.deck = func(self.deck)

    def _make_deck(self) -> None:
        pass

    def _make_full_suit(self, value: Tuple[Type[CardValue], int]) -> List[Card]:
        return [x(value[0](value[1])) for x in suit_list]

    def _set_card_value_dict(self):
        for card in self.deck:
            self.cards_value[type(card.value)] = card.value.value


class Deck32(Deck):
    def _make_deck(self) -> None:
        if not self.deck:
            for i in card_list[:9]:
                self.deck.extend(self._make_full_suit(i))


class Deck52(Deck):
    def _make_deck(self) -> None:
        if not self.deck:
            for i in card_list:
                self.deck.extend(self._make_full_suit(i))



class CustomDeck(Deck):
    def __init__(self, cards: Iterable[Card]) -> None:
        super().__init__(cards)


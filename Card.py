from CardValue import CardValue
from typing import Optional

def draw_card(card: "Card"):
    card_template = f"""
    ┌─────────┐
    │ {str(card.value):<2}      │
    │         │
    │    {str(card)}    │
    │         │
    │      {str(card.value):>2} │
    └─────────┘
    """
    return card_template

class Card:
    def __init__(self, value: CardValue):
        self.value = value
        self.image_for_console: str = draw_card(self)

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __repr__(self):
        return f'({self.__class__.__name__}, {repr(self.value)})'


class Heart(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)

    def __str__(self):
        return f"{"♥"}"


class Spade(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)

    def __str__(self):
        return f"{"♠"}"

class Diamond(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)

    def __str__(self):
        return f"{"♦"}"

class Club(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)

    def __str__(self):
        return f"{"♣"}"


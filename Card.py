from CardValue import CardValue

class Card:
    def __init__(self, value: CardValue):
        self.value = value
        self.status: str = ""


    def __repr__(self):
        return f'({self.__class__.__name__}, {repr(self.value)})'

class Heart(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)



class Spade(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)


class Diamond(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)


class Club(Card):
    def __init__(self, value: CardValue):
        super().__init__(value)


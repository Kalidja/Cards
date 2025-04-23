

class CardValue:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Jocker(CardValue):
    def __init__(self, value: int):
        super().__init__(13)


class Ace(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class King(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Queen(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Jack(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Ten(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Nine(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Eight(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Seven(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Six(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Five(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Four(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Three(CardValue):
    def __init__(self, value: int):
        super().__init__(value)


class Two(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

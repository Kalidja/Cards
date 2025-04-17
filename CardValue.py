

class CardValue:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Jocker(CardValue):
    def __init__(self):
        super().__init__(13)


class Ace(CardValue):
    def __init__(self):
        super().__init__(12)


class King(CardValue):
    def __init__(self):
        super().__init__(11)


class Queen(CardValue):
    def __init__(self):
        super().__init__(10)


class Jack(CardValue):
    def __init__(self):
        super().__init__(9)


class Ten(CardValue):
    def __init__(self):
        super().__init__(8)


class Nine(CardValue):
    def __init__(self):
        super().__init__(7)


class Eight(CardValue):
    def __init__(self):
        super().__init__(6)


class Seven(CardValue):
    def __init__(self):
        super().__init__(5)


class Six(CardValue):
    def __init__(self):
        super().__init__(4)


class Five(CardValue):
    def __init__(self):
        super().__init__(3)


class Four(CardValue):
    def __init__(self):
        super().__init__(2)


class Three(CardValue):
    def __init__(self):
        super().__init__(1)


class Two(CardValue):
    def __init__(self):
        super().__init__(0)

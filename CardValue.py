

class CardValue:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Jocker(CardValue):
    def __init__(self, value: int):
        super().__init__(13)

    def __str__(self):
        return f'{"Jocker"}'

class Ace(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"A"}'

class King(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"K"}'

class Queen(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"Q"}'

class Jack(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"J"}'

class Ten(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"10"}'

class Nine(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"9"}'

class Eight(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"8"}'

class Seven(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"7"}'

class Six(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"6"}'

class Five(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"5"}'

class Four(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"4"}'

class Three(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"3"}'

class Two(CardValue):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{"2"}'

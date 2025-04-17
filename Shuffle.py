from Card import Card
from typing import List
from random import randint


class Shuffle:
    @staticmethod
    def over_hand(deck: List[Card]) -> List[Card]:
        "сбрасывать n первых карт и класть вниз. Повторить m раз"

        index = 0
        right = []
        for i in range(0, randint(15,20)):
            for j in range(5):
                try:
                    n = randint(3,6)
                    right = deck[index : index + n] + right
                    index += n
                except IndexError as e:
                    right = deck[index:] + right
            deck = right
            right = []
            index = 0
        return deck


    @staticmethod
    def swing_card(deck: List[Card]) -> List[Card]:
        "разделить на 2 стопки, левую разделять еще на 2, и еще раз"


        n = randint(7, 10)
        index = 0
        for i in range(0, n):
            left = deck[len(deck) // 2:]
            right = deck[:len(deck) // 2]
            for j in range(3):
                m = (len(left) - index) // 2 + index
                right = left[index: m] + right
                index = (len(left) + index) // 2
            right += left[index:]
            index = 0
            deck = right
        return deck

    @staticmethod
    def charlier_cut(deck: List[Card]) -> List[Card]:
        "половин менять местами"

        half = len(deck) // 2
        quatro = half // 2
        n = randint(half - randint(quatro, half), half - 1)
        return deck[n:] + deck[:n]


    @staticmethod
    def riffle_shuffle(deck: List[Card]) -> List[Card]:
        "разделить на 2, первый из первыой + первый из второй и т.д."

        half = len(deck) // 2
        res = []
        for j in range(0, half):
            res.append(deck[j])
            res.append(deck[j + half])
        return res





'''"""l = [1,2,3,4,5,6,7]
print(l[3:] + l[:3])"""
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
res = Shuffle.riffle_shuffle(l)
print(res)

print("Длина оригинала и результата:", True if len(l) == len(res) else False)
print("Длина set:", True if len(set(l)) == len(set(res)) else False)
print("Одинаково наполнение set:", set(l) == set(res))'''
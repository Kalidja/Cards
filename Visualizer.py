from Card import Card
from typing import List, Dict
from Persons import Person

def visualize(cards: Dict[Person, List[Card]], same_level: bool = False):
    for i in cards:
        print(i.name)
        for j in cards[i]:
            print(j.image_for_console) if not same_level else print(j.image_for_console, end=' ')

def visualize_player_hand(player: Person, same_level: bool = False):
    for i in player.hand:
        print(i.image_for_console) if not same_level else print(i.image_for_console, end=' ')

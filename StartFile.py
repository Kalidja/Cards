from Games import TheDrunkard
from Table import Table
from Persons.Player import Player
import Deck

game = TheDrunkard.TheDrunkard(Deck.Deck())

p1 = Player("p1")
p2 = Player("p2")
p3 = Player("p3")
p4 = Player("p4")


table = Table(0, game=game)
table.add_new_player(p1)
table.add_new_player(p2)
table.add_new_player(p3)
table.add_new_player(p4)
table.start_game()
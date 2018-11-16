from card import Card

class Deck:
    
    def __init__(self):
        self.cards = []
        self.populate()
        print(self._cards)

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers]

my_deck = Deck()
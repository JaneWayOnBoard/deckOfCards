class Card:
    
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self.number + " of " + self.suit
    
    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A"]:
            self._number = number
        else:
            print("That's not a card!")

 

my_card = Card("hearts", "6")
my_card.suit = "clubs"
another_card = Card("Dinosaurs", "1")

print(my_card)
print(another_card)
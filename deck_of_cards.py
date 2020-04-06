import random

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        for s in Deck.suits:
           for v in Deck.values:
               self.cards.append(Card(s,v))

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self, num):
        
        cards_removed = []

        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        for n in range(0,(min(self.count(), num))):
            cards_removed.append(self.cards.pop(-1))
        return cards_removed

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")
        return self.cards

    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, num):
        return self._deal(num)
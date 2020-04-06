from deck_of_cards import Card
from deck_of_cards import Deck
import unittest

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", "A")

    def test_suit(self):
        self.assertEqual(self.card1.suit, "Spades")
    
    def test_value(self):
        self.assertEqual(self.card1.value, "A")

    def test_repr(self):
        self.assertEqual(str(self.card1), "A of Spades")

class DeckTest(unittest.TestCase):

    def setUp(self):
        self.deck1 = Deck()
    
    def test_deck_creation(self):
        self.assertEqual(len(self.deck1.cards), 52)

    def test_repr_deck(self):
        self.assertEqual(str(self.deck1), "Deck of 52 cards")
    
    def test_count(self):
        self.assertEqual(self.deck1.count(), len(self.deck1.cards))

    def test_shuffle_keeps_cards(self):
        self.deck1.shuffle()
        self.assertEqual(len(self.deck1.cards), 52)

    def test_shuffle_error(self):
        self.deck1.cards.pop()
        with self.assertRaises(ValueError):
            self.deck1.shuffle()

    def test_deal_card(self):
        self.deck1.deal_card()
        self.assertEqual(len(self.deck1.cards), 51)

    def test_deal_hand(self):
        self.deck1.deal_hand(4)
        self.assertEqual(len(self.deck1.cards), 48)


if __name__ == "__main__":
    unittest.main()

import unittest

# http://dojopuzzles.com/problemas/exibe/poker/

# Spades (highest)
# Hearts
# Diamonds
# Clubs (lowest)

# 2..9 (each one with their own value)
# T = 10
# J = 11
# Q = 12
# K = 13
# A = 14

# Royal Flush
# Straight Flush
# Four of a Kind
# Full House
# Flush
# Straight
# Three of a kind
# Two Pair
# One Pair
# High Card

# 'RoyalFlush %s'         % self.first.suit
# 'StraightFlush %s'      % self.first
# 'FullHouse %s'          % self.first.letter
# 'Flush %s'              % self.first.suit
# 'Straight %s'           % self.first
# 'ThreeOfAKind %s:%s:%s' % (self.first, self.second, self.third)
# 'TwoPair %s:%s:%s:%s'   % (self.first, self.second, self.third, self.fourth)
# 'Pair %s:%s'            % (self.first, self.second)
# 'High %s'               % self.first


############ CONTINUE HERE ############
# class TestHandCompare(unittest.TestCase):
#     def setUp(self):
#         self.hand_p1 = None
#         self.hand_p2 = None

#     def test_high_card(self):
#         self.hand_p1 = Hand([Card('7S'), Card('5S'), Card('4H'), Card('3S'), Card('2S')])
#         self.hand_p2 = Hand([Card('7S'), Card('5S'), Card('4H'), Card('3S'), Card('2S')])
        
#         self.assertTrue(self.hand_p1 > self.hand_p2)


class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = None

    def test_high_card(self):
        self.hand = Hand([Card('7S'), Card('5S'), Card('4H'), Card('3S'), Card('2S')])
        self.assertEqual('High 7S', self.hand.get_hand())

    def test_one_pair(self):
        self.hand = Hand([Card('7S'), Card('7H'), Card('4S'), Card('3S'), Card('2S')])
        self.assertEqual('Pair 7S:7H', self.hand.get_hand())

    def test_two_pair(self):
        self.hand = Hand([Card('7S'), Card('7H'), Card('4S'), Card('4H'), Card('2S')])
        self.assertEqual('TwoPair 7S:7H:4S:4H', self.hand.get_hand())

    def test_three_of_a_kind(self):
        self.hand = Hand([Card('7S'), Card('7H'), Card('7D'), Card('4H'), Card('2S')])
        self.assertEqual('ThreeOfAKind 7S:7H:7D', self.hand.get_hand())

    def test_straight(self):
        self.hand = Hand([Card('6S'), Card('5S'), Card('4H'), Card('3S'), Card('2S')])
        self.assertEqual('Straight 6S', self.hand.get_hand())

    def test_flush(self):
        self.hand = Hand([Card('9S'), Card('6S'), Card('4S'), Card('3S'), Card('2S')])
        self.assertEqual('Flush S', self.hand.get_hand())

    def test_full_house(self):
        self.hand = Hand([Card('9S'), Card('9H'), Card('9D'), Card('3S'), Card('3H')])
        self.assertEqual('FullHouse 9', self.hand.get_hand())

    def test_four_of_a_kind(self):
        self.hand = Hand([Card('9S'), Card('9H'), Card('9D'), Card('9C'), Card('3H')])
        self.assertEqual('FourOfAKind 9', self.hand.get_hand())

    def test_straight_flush(self):
        self.hand = Hand([Card('9S'), Card('8S'), Card('7S'), Card('6S'), Card('5S')])
        self.assertEqual('StraightFlush 9S', self.hand.get_hand())

    def test_royal_flush(self):
        self.hand = Hand([Card('AS'), Card('KS'), Card('QS'), Card('JS'), Card('TS')])
        self.assertEqual('RoyalFlush S', self.hand.get_hand())


class Hand:

    def __init__(self, hand_cards_list_ordered):
        self.cards = hand_cards_list_ordered
        self.first = self.cards[0]
        self.second = self.cards[1]
        self.third = self.cards[2]
        self.fourth = self.cards[3]
        self.fifth = self.cards[4]

    def __cmp__(self, obj):
        pass

    def get_hand(self):
        if self._is_royal_flush():
            return 'RoyalFlush %s' % self.first.suit
        if self._is_straight_flush():
            return 'StraightFlush %s' % self.first
        if self._is_four_of_a_kind():
            return 'FourOfAKind %s' % self.first.letter
        if self._is_full_house():
            return 'FullHouse %s' % self.first.letter
        if self._is_flush():
            return 'Flush %s' % self.first.suit
        if self._is_straight():
            return 'Straight %s' % self.first
        if self._is_three_of_a_kind():
            return 'ThreeOfAKind %s:%s:%s' % (self.first, self.second, self.third)
        if self._is_two_pairs():
            return 'TwoPair %s:%s:%s:%s' % (self.first, self.second, self.third, self.fourth)
        if self._is_pair():
            return 'Pair %s:%s' % (self.first, self.second)
        return self._high_card()

    def _is_royal_flush(self):
        return self._is_straight_flush and self.first.letter == 'A'

    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        return self._is_three_of_a_kind() and self.third.letter_value == self.fourth.letter_value

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self.fourth.letter_value == self.fifth.letter_value

    def _is_flush(self):
        return self.first.suit_value == self.second.suit_value \
            == self.third.suit_value == self.fourth.suit_value \
            == self.fifth.suit_value

    def _is_straight(self):
        return self.fifth.letter_value + 1 == self.fourth.letter_value \
            and self.fourth.letter_value + 1 == self.third.letter_value \
            and self.third.letter_value + 1 == self.second.letter_value \
            and self.second.letter_value + 1 == self.first.letter_value

    def _is_three_of_a_kind(self):
        return self.first.letter_value == self.second.letter_value == self.third.letter_value

    def _is_two_pairs(self):
        return self._is_pair() and self.third.letter_value == self.fourth.letter_value

    def _is_pair(self):
        return self.first.letter_value == self.second.letter_value

    def _high_card(self):
        return 'High %s' % self.first



class TestCardValue(unittest.TestCase):

    def test_equal_letters_equal_suits(self):
        self.assertEqual(Card('AS'), Card('AS'))

    def test_equal_letters_different_suits(self):
        self.assertTrue(Card('AS') > Card('AH'))
        self.assertTrue(Card('AH') > Card('AD'))
        self.assertTrue(Card('AD') > Card('AC'))
        self.assertFalse(Card('AC') > Card('AS'))

    def test_different_letters_equal_suits(self):
        self.assertTrue(Card('AS') > Card('KS'))
        self.assertTrue(Card('KS') > Card('QS'))
        self.assertTrue(Card('QS') > Card('JS'))
        self.assertTrue(Card('JS') > Card('TS'))
        self.assertTrue(Card('TS') > Card('9S'))
        self.assertTrue(Card('9S') > Card('8S'))
        self.assertTrue(Card('8S') > Card('7S'))
        self.assertTrue(Card('7S') > Card('6S'))
        self.assertTrue(Card('6S') > Card('5S'))
        self.assertTrue(Card('5S') > Card('4S'))
        self.assertTrue(Card('4S') > Card('3S'))
        self.assertTrue(Card('3S') > Card('2S'))
        self.assertFalse(Card('2S') > Card('AS'))

    def test_different_letters_different_suits(self):
        self.assertTrue(Card('AS') > Card('KH'))
        self.assertFalse(Card('2S') > Card('AH'))
        # need? no, right? or what else?


class TestCardLetterValue(unittest.TestCase):

    def tests_with_numeric_values(self):
        self.assertEqual(2, Card('2S').letter_value)
        self.assertEqual(3, Card('3S').letter_value)
        self.assertEqual(4, Card('4S').letter_value)
        self.assertEqual(5, Card('5S').letter_value)
        self.assertEqual(6, Card('6S').letter_value)
        self.assertEqual(7, Card('7S').letter_value)
        self.assertEqual(8, Card('8S').letter_value)
        self.assertEqual(9, Card('9S').letter_value)

    def test_T_letter(self):
        self.assertEqual(10, Card('TS').letter_value)

    def test_J_letter(self):
        self.assertEqual(11, Card('JS').letter_value)

    def test_Q_letter(self):
        self.assertEqual(12, Card('QS').letter_value)

    def test_K_letter(self):
        self.assertEqual(13, Card('KS').letter_value)

    def test_A_letter(self):
        self.assertEqual(14, Card('AS').letter_value)


class TestCardSuitValue(unittest.TestCase):

    def test_S_suit(self):
        self.assertEqual(4, Card('2S').suit_value)
    
    def test_H_suit(self):
        self.assertEqual(3, Card('2H').suit_value)
    
    def test_D_suit(self):
        self.assertEqual(2, Card('2D').suit_value)
    
    def test_C_suit(self):
        self.assertEqual(1, Card('2C').suit_value)


class Card:
    LETTER_VALUES = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    SUITS_VALUES = {'S': 4, 'H': 3, 'D': 2, 'C': 1}

    def __init__(self, full_card_value):
        self.card = full_card_value
        self.letter = self.card[0]
        self.suit = self.card[1]

    def __str__(self):
        return self.card

    def __cmp__(self, obj):
        if self.letter_value == obj.letter_value:
            return self.suit_value > obj.suit_value
        return self.letter_value > obj.letter_value

    @property
    def letter_value(self):
        try:
            return int(self.letter)
        except ValueError:
            return Card.LETTER_VALUES[self.letter]

    @property
    def suit_value(self):
        return Card.SUITS_VALUES[self.suit]


if __name__ == '__main__':
    unittest.main()

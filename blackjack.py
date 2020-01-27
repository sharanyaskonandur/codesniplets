'''
Blackjack I
'''

import unittest

# catalog of values for each card
card_values = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10,
               'k': 10}


# function for black jack advice
def black_jack(crd1, crd2, crd3):
    crd_total = (card_values[crd1] + card_values[crd2] + card_values[crd3])  # calculate total value of cards

    if crd_total > 21:  # if total value is over 21, print already busted
        return ("Already busted.")
    elif crd_total == 21:  # if total value is 21, print 'Blackjack'
        return ("Blackjack!")
    elif crd_total >= 17:  # if total value is greater than or equal to 17, print 'stay'
        return ("Stay")
    elif crd_total < 17:  # if total value is under 17, print 'hit'
        return ("Hit")


# user input loop
# while True:
#     card_1 = input('What\'s your first card? ')  # if
#     if card_1 == 'done':
#         break
#     elif card_1 not in card_values:
#         print("Invalid card.")
#         continue
#     else:
#         pass
#     card_2 = input('What\'s your second card? ')
#     if card_2 == 'done':
#         break
#     elif card_2 not in card_values:
#         print("Invalid card.")
#         continue
#     else:
#         pass
#     card_3 = input('What\'s your third card? ')
#     if card_3 == 'done':
#         break
#     elif card_3 not in card_values:
#         print("Invalid card.")
#         continue
#     else:
#         pass
#     black_jack(card_1, card_2, card_3)

# unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_aj6(self):
        self.assertEqual(black_jack('a', 'j', '6'), 'Stay')

    def test_jkq(self):
        self.assertEqual(black_jack('j', 'k', 'q'), 'Already busted.')

    def test_10ja(self):
        self.assertEqual(black_jack('10', 'j', 'a'), 'Blackjack!')

    def test_a23(self):
        self.assertEqual(black_jack('a', '2', '3'), 'Hit')


if __name__ == '__main__':
    unittest.main()
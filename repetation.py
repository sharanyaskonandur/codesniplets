'''
 Write a function that returns the number of occurances of 'hi' in a given string.
'''

import unittest


# Count hi function - Start counter. Start loop for the range of the length of input string. If the characters starting
# at the iteration and ending two chars (length of 'hi' ahead) match 'hi', iterate counter. When done, return counter
def count_hi(hi_hi):
    counter = 0
    for i in range(len(hi_hi)):
        if hi_hi[i:i + 2] == 'hi':
            counter += 1
    return counter


# Prompt for repeating 'hi's.
input_hi = input("Type 'hihihi...': ")


# Pass input string to function and print result
# print(count_hi(input_hi))

class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_01(self):
        self.assertEqual(count_hi('hihihihihihihihihi'), 9)

    def test_02(self):
        self.assertEqual(count_hi('asdas'), 0)

    def test_03(self):
        self.assertEqual(count_hi('hihi'), 2)

    def test_04(self):
        self.assertEqual(count_hi('ihihihihihihihihihihhhhhihihihi'), 13)


if __name__ == '__main__':
    unittest.main()
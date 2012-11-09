# Input data: contains four integer numbers:
#
# - the initial Sofia's offer,
# - Sofia's raise to his offer,
# - the initial fare required by the old man's,
# - the old man's reduction of his fare;
#
# Output data: the amount of money that Sofia will pay for the spaceship.

import unittest

def checkio(offers):
    initial_petr, raise_petr, initial_driver, reduction_driver = offers
    offer_petr = initial_petr
    offer_driver = initial_driver
    i=1
    while offer_petr < offer_driver:
        offer_petr = initial_petr + i*raise_petr
        offer_driver = initial_driver - i*reduction_driver
        i = i + 1
    return offer_petr

class ChekioTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(checkio([150, 50, 1000, 100]), 450)

    def test_2(self):
        self.assertEquals(checkio([150, 50, 900, 100]), 400)

if __name__ == '__main__':
    unittest.main(failfast=False)

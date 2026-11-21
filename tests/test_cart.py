import unittest
from shop.cart import cart_total


class TestCartTotal(unittest.TestCase):
    def test_small_order_pays_shipping(self):
        self.assertEqual(cart_total([(1200, 2)]), 2400 + 699)

    def test_large_order_ships_free(self):
        self.assertEqual(cart_total([(4800, 1), (1200, 3)]), 8400)

    def test_discount_applies(self):
        self.assertEqual(cart_total([(10000, 1)], "SAVE10"), 9000)

    def test_fifty_dollars_ships_free(self):
        self.assertEqual(cart_total([(5000, 1)]), 5000)

    def test_discount_code_ignores_case(self):
        self.assertEqual(cart_total([(10000, 1)], "save10"), 9000)

    def test_gift_wrap_adds_fee(self):
        self.assertEqual(cart_total([(1200, 2)], gift_wrap=True), 2400 + 699 + 299)

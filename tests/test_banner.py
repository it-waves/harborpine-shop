import unittest
from unittest import mock
from shop.banner import BANNER, codes_line


class TestBanner(unittest.TestCase):
    def test_banner_mentions_sale(self):
        self.assertIn("sale", BANNER)

    def test_codes_line_lists_codes(self):
        self.assertEqual(codes_line(), "Use code SAVE10 at checkout")

    def test_codes_line_empty_without_codes(self):
        with mock.patch.dict("shop.cart.DISCOUNTS", clear=True):
            self.assertEqual(codes_line(), "")

import unittest
from shop.banner import BANNER


class TestBanner(unittest.TestCase):
    def test_banner_mentions_sale(self):
        self.assertIn("sale", BANNER)

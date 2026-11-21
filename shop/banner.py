from shop.cart import DISCOUNTS

BANNER = 'Winter sale'
BANNER_COLOR = 'red'


def codes_line():
    """One line for the banner that lists every discount code."""
    return f"Use code {' or '.join(DISCOUNTS)} at checkout"

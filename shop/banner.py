from shop.cart import DISCOUNTS

BANNER = 'Winter sale'
BANNER_COLOR = 'darkred'


def codes_line():
    """One line for the banner that lists every discount code."""
    if not DISCOUNTS:
        return ""
    return f"Use code {' or '.join(DISCOUNTS)} at checkout"

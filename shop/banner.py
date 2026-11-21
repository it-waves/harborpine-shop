from shop.cart import DISCOUNTS

BANNER = 'Winter sale is on'
BANNER_COLOR = 'darkred'
STORE_HOURS = '9am to 7pm'


def codes_line():
    """One line for the banner that lists every discount code."""
    if not DISCOUNTS:
        return ""
    return f"Use code {' or '.join(DISCOUNTS)} at checkout"

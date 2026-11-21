FREE_SHIPPING_OVER = 5000  # cents ($50)
FLAT_SHIPPING = 699  # cents ($6.99)
DISCOUNTS = {"SAVE10": 10}
GIFT_WRAP_FEE = 299  # cents, optional gift wrap


def _apply_discount(subtotal, code):
    if code in DISCOUNTS:
        return subtotal - subtotal * DISCOUNTS[code] // 100
    return subtotal


def cart_total(items, discount_code=None, gift_wrap=False):
    """Return the order total in cents.

    items: list of (price_in_cents, quantity)
    """
    subtotal = sum(price * qty for price, qty in items)
    code = (discount_code or "").strip().upper()
    subtotal = _apply_discount(subtotal, code)
    shipping = 0 if subtotal >= FREE_SHIPPING_OVER else FLAT_SHIPPING
    wrap = GIFT_WRAP_FEE if gift_wrap else 0
    return subtotal + shipping + wrap

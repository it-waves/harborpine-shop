FREE_SHIPPING_OVER = 5000  # cents ($50)
FLAT_SHIPPING = 699
DISCOUNTS = {"SAVE10": 10}


def cart_total(items, discount_code=None):
    """Return the order total in cents."""
    subtotal = sum(price * qty for price, qty in items)
    code = (discount_code or "").upper()
    if code in DISCOUNTS:
        subtotal -= subtotal * DISCOUNTS[code] // 100
    shipping = 0 if subtotal >= FREE_SHIPPING_OVER else FLAT_SHIPPING
    return subtotal + shipping

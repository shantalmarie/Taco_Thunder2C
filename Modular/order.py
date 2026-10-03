# ============================================================
# TACO THUNDER - ORDER
# ============================================================

from inputs import (
    get_menu_item,
    get_quantity,
    ask_yes_no
)

from display import (
    print_divider,
    print_success
)


def take_order():
    """Collect items and quantities from the customer."""

    cart = []

    while True:

        print_divider()

        print("   ADD ITEM TO YOUR ORDER")
        print()

        # Get menu item
        code, item_data = get_menu_item()

        # Get quantity
        quantity = get_quantity()

        # Add item to cart
        cart.append({
            "code": code,
            "name": item_data["name"],
            "price": item_data["price"],
            "quantity": quantity
        })

        print_success(
            f"Added {quantity}x "
            f"{item_data['name']} "
            f"to your order!"
        )

        # Ask if customer wants another item
        if not ask_yes_no(
            "Would you like to order another item?"
        ):
            break

    return cart

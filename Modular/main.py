# ============================================================
# TACO THUNDER - MAIN MODULE
# ============================================================

from display import (
    print_header,
    print_menu,
    print_goodbye,
    print_divider
)

from inputs import ask_yes_no

from order import take_order

from receipt import print_receipt


# ------------------------------------------------------------
# DISPLAY WELCOME
# ------------------------------------------------------------

def display_welcome():
    """
    Displays the restaurant header and menu.
    Returns True if the customer wants to order.
    """

    print_header()
    print_menu()

    return ask_yes_no(
        "Would you like to place an order?"
    )


# ------------------------------------------------------------
# PROCESS ORDER
# ------------------------------------------------------------

def process_order():
    """
    Gets the customer's order and displays the receipt.
    """

    cart = take_order()

    if not cart:
        print("\nNo items were ordered.")
        return

    print_divider()

    print_receipt(cart)


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():
    """
    Main controller of the TACO THUNDER ordering system.
    """

    try:

        # Display welcome screen and menu
        wants_to_order = display_welcome()

        # Customer does not want to order
        if not wants_to_order:
            print_goodbye()
            return

        # Process the customer's order
        process_order()

        # Display goodbye message
        print_goodbye()

    except KeyboardInterrupt:

        print("\n\nOrder cancelled by user.")
        print_goodbye()


# ------------------------------------------------------------
# MODULE ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
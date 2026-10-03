# ============================================================
# TACO THUNDER - INPUTS
# ============================================================

from data import MENU
from display import print_error


def get_menu_item():
    """Ask the user for a valid menu item."""

    while True:

        try:
            code = input("  Enter menu item number: ").strip()

            for category, items in MENU.items():

                if code in items:
                    return code, items[code]

            print_error(
                f"Item '{code}' not found. Please check the menu."
            )

        except (EOFError, KeyboardInterrupt):

            print_error(
                "Invalid input. Please try again."
            )


def get_quantity():
    """Ask the user for a valid quantity."""

    while True:

        try:
            qty_input = input("  Enter quantity: ").strip()

            qty = int(qty_input)

            if qty <= 0:
                print_error(
                    "Quantity must be at least 1."
                )
                continue

            if qty > 50:
                print_error(
                    "For orders over 50, please contact catering."
                )
                continue

            return qty

        except ValueError:

            print_error(
                "Please enter a valid whole number."
            )


def ask_yes_no(prompt):
    """Ask a yes/no question."""

    while True:

        try:
            response = input(
                f"  {prompt} (Y/N): "
            ).strip().lower()

            if response in (
                "y",
                "yes",
                "yeah",
                "yep",
                "sure"
            ):
                return True

            elif response in (
                "n",
                "no",
                "nope",
                "nah",
                "pass"
            ):
                return False

            else:
                print_error(
                    "Please enter 'Y' for Yes or 'N' for No."
                )

        except (EOFError, KeyboardInterrupt):

            print_error(
                "Invalid input. Please try again."
            )
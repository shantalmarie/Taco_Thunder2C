# ============================================================
# TACO THUNDER - DISPLAY
# ============================================================

from data import MENU


def print_header():
    """Print restaurant header."""

    print("╔" + "═" * 56 + "╗")
    print("║" + " " * 16 + " TACO THUNDER " + " " * 19 + "║")
    print("║" + " " * 15 + "Bold. Spicy. Unstoppable." + " " * 14 + "║")
    print("╚" + "═" * 56 + "╝")
    print()


def print_menu():
    """Display the complete menu."""

    print("┌" + "─" * 56 + "┐")
    print("│" + " " * 17 + "📋  M E N U  B O A R D" + " " * 17 + "│")
    print("├" + "─" * 56 + "┤")

    for category, items in MENU.items():

        category_text = category.upper()

        print(f"│  {category_text:<52}│")
        print("│" + " " * 56 + "│")

        for code, item in items.items():

            name = item["name"]
            price = item["price"]

            item_text = f"     [{code}] {name}"
            price_text = f"₱{price:,.2f}"

            spaces = 56 - len(item_text) - len(price_text)

            if spaces < 1:
                spaces = 1

            print(
                f"│{item_text}"
                + " " * spaces
                + f"{price_text}│"
            )

        print("│" + " " * 56 + "│")

    print("└" + "─" * 56 + "┘")
    print()


def print_divider():
    """Print a divider."""

    print("\n" + "•" * 58 + "\n")


def print_error(message):
    """Print an error message."""

    print(f"\n  ⚠️ ERROR: {message}")


def print_success(message):
    """Print a success message."""

    print(f"\n  ✓ {message}")


def print_goodbye():
    """Print goodbye message."""

    print("\n" + "╔" + "═" * 56 + "╗")
    print(
        "║"
        + " " * 15
        + "Thanks for rolling with Taco Thunder!"
        + " " * 3
        + "║"
    )
    print(
        "║"
        + " " * 17
        + "Stay spicy, amigo! "
        + " " * 14
        + "║"
    )
    print("╚" + "═" * 56 + "╝")
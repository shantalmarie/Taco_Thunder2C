# ============================================================
# TACO THUNDER - RECEIPT
# ============================================================

from datetime import datetime

from data import (
    DISCOUNT_RATES,
    TAX_RATE
)


def calculate_totals(cart):
    """Calculate subtotal, discount, tax, and grand total."""

    subtotal = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    total_items = sum(
        item["quantity"]
        for item in cart
    )

    discount_rate = 0
    discount_name = "None"

    # Check discount tiers
    for tier, config in DISCOUNT_RATES.items():

        if (
            tier == "bulk"
            and total_items >= config["threshold"]
        ):

            if config["rate"] > discount_rate:

                discount_rate = config["rate"]

                discount_name = (
                    f"Bulk Order "
                    f"({total_items} items)"
                )

        elif (
            tier in ("premium", "vip")
            and subtotal >= config["threshold"]
        ):

            if config["rate"] > discount_rate:

                discount_rate = config["rate"]

                discount_name = (
                    f"{tier.title()} Tier "
                    f"(₱{subtotal:,.2f})"
                )

    discount_amount = subtotal * discount_rate

    taxable_amount = (
        subtotal - discount_amount
    )

    tax_amount = (
        taxable_amount * TAX_RATE
    )

    grand_total = (
        taxable_amount + tax_amount
    )

    return (
        subtotal,
        discount_rate,
        discount_name,
        discount_amount,
        tax_amount,
        grand_total
    )


def print_receipt(cart):
    """Print the final receipt."""

    if not cart:
        print("\n  No items ordered.")
        print("  Receipt cancelled.")
        return

    (
        subtotal,
        discount_rate,
        discount_name,
        discount_amount,
        tax_amount,
        grand_total
    ) = calculate_totals(cart)

    now = datetime.now()

    print("\n" + "=" * 48)

    print("       TACO THUNDER")
    print("       456 Fiesta Avenue, Spice District")
    print("       Tel: (02) 8987-6543")

    print("-" * 48)

    print(
        f"  Date: {now.strftime('%Y-%m-%d')}"
    )

    print(
        f"  Time: {now.strftime('%H:%M:%S')}"
    )

    print("  Cashier: SYSTEM-AUTO")

    print(
        f"  Transaction #: "
        f"TXN-{now.strftime('%Y%m%d%H%M%S')}"
    )

    print("-" * 48)

    print(
        "  QTY  ITEM                          PRICE"
    )

    print("-" * 48)

    for item in cart:

        item_total = (
            item["price"] * item["quantity"]
        )

        name = item["name"][:26]

        print(
            f"  {item['quantity']:<4} "
            f"{name:<26} "
            f"₱{item_total:>8,.2f}"
        )

        print(
            f"       @ "
            f"₱{item['price']:,.2f} each"
        )

    print("-" * 48)

    print(
        f"  Subtotal:"
        f"{' ' * 29}"
        f"₱{subtotal:>8,.2f}"
    )

    if discount_rate > 0:

        print(
            f"  Discount ({discount_name}): "
            f"-₱{discount_amount:>8,.2f}"
        )

    print(
        f"  Tax ({TAX_RATE * 100:.0f}% VAT):"
        f"{' ' * 26}"
        f"₱{tax_amount:>8,.2f}"
    )

    print("-" * 48)

    print(
        f"  TOTAL:"
        f"{' ' * 32}"
        f"₱{grand_total:>8,.2f}"
    )

    print("=" * 48)

    print(
        "  Gracias amigo! "
        "Come back pronto! 🙏"
    )

    print("=" * 48)
# ============================================================
# TACO THUNDER - DATA
# ============================================================

RESTAURANT_NAME = "TACO THUNDER"
RESTAURANT_ADDRESS = "456 Fiesta Avenue, Spice District"
RESTAURANT_PHONE = "(02) 8987-6543"

MENU = {
    "Tacos": {
        "1": {"name": "Classic Beef Taco", "price": 89.00},
        "2": {"name": "Spicy Chicken Taco", "price": 99.00},
        "3": {"name": "Grilled Fish Taco", "price": 119.00},
        "4": {"name": "Veggie Fiesta Taco", "price": 79.00},
    },

    "Burritos": {
        "5": {"name": "Steak Burrito (Regular)", "price": 169.00},
        "6": {"name": "Steak Burrito (Large)", "price": 219.00},
        "7": {"name": "Bean & Cheese Burrito", "price": 129.00},
        "8": {"name": "Breakfast Burrito", "price": 149.00},
    },

    "Sides": {
        "9": {"name": "Nachos Supreme", "price": 139.00},
        "10": {"name": "Mexican Rice Bowl", "price": 89.00},
        "11": {"name": "Street Corn (Elote)", "price": 79.00},
        "12": {"name": "Chips & Salsa", "price": 59.00},
    },

    "Drinks & Desserts": {
        "13": {"name": "Horchata", "price": 69.00},
        "14": {"name": "Mango Agua Fresca", "price": 75.00},
        "15": {"name": "Churros (3 pcs)", "price": 89.00},
    }
}


DISCOUNT_RATES = {
    "bulk": {
        "threshold": 5,
        "rate": 0.05
    },

    "premium": {
        "threshold": 500,
        "rate": 0.10
    },

    "vip": {
        "threshold": 1000,
        "rate": 0.15
    }
}


TAX_RATE = 0.12
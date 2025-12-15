"""
hospital_logic.py
Handles logic using Array Indexing.
"""
import config

def get_service_index(code):
    """
    Searches for the code in the array.
    Returns the INDEX if found, or -1 if not found.
    """
    # Manual Linear Search
    for i in range(len(config.SERVICE_CODES)):
        if config.SERVICE_CODES[i] == code:
            return i
    return -1

def calculate_discount(subtotal, age):
    #Applies 20% discount if age >= 60.
    if age >= config.SENIOR_AGE_LIMIT:
        disc = subtotal * config.SENIOR_DISCOUNT
        print(f"\n[Benefit] Senior Citizen Discount (20%): -Rs. {disc:.2f}")
        return disc
    return 0.0

def calculate_tax(amount):
    #Calculates GST.
    return amount * config.GST_RATE
"""
logic.py
Handles the math for discounts, tax, and promos.
"""
import config

def check_promo(code, price):
    #Challenge 30: Apply Promo Code
    if code.upper() == "PROMO10":
        return price * 0.90, True # Return new price and a flag
    return price, False

def apply_discounts(grand_total, total_qty, is_member):
    #Challenges 27 & 28: Apply all discounts
    print("\n--- Applying Discounts ---")
    
    # Rule 1: High Value (> 10,000)
    if grand_total > config.HIGH_VALUE_LIMIT:
        disc = grand_total * config.HIGH_VALUE_RATE
        grand_total -= disc
        print(f"[Discount] High Value (10%): -Rs. {disc:.2f}")

    # Rule 2: Bulk Quantity (> 20 items)
    if total_qty > config.BULK_QTY_LIMIT:
        disc = grand_total * config.BULK_QTY_RATE
        grand_total -= disc
        print(f"[Discount] Bulk Qty (5%):    -Rs. {disc:.2f}")

    # Rule 3: Membership
    if is_member == 'y':
        disc = grand_total * config.MEMBER_RATE
        grand_total -= disc
        print(f"[Discount] Member (2%):      -Rs. {disc:.2f}")
        
    return grand_total

def calculate_tax(amount):
    #Challenge 29: Tiered Tax
    if amount < config.TAX_LIMIT_LOW:
        rate = 0.05
    elif amount <= config.TAX_LIMIT_HIGH:
        rate = 0.10
    else:
        rate = 0.15
        
    tax_amt = amount * rate
    return tax_amt, rate
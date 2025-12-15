"""
main.py
The main loop for the Retail Shopping App.
"""
import config
import logic

def main():
    print(" Retail Shopping System ")
    
    cart = []
    total_qty = 0
    grand_total = 0.0
    
    #  CHALLENGE 26: Input Loop 
    while True:
        print("\nEnter Item Details:")
        code = input("  Code (e.g., PROMO10): ").strip()
        desc = input("  Description: ").strip()
        qty = int(input("  Quantity: "))
        price = float(input("  Unit Price: "))
        
        #  CHALLENGE 30: Check Promo 
        price, applied = logic.check_promo(code, price)
        if applied:
            print("  * PROMO10 Applied! 10% Off this item.")
            
        # Calculate Item Total
        item_total = price * qty
        grand_total += item_total
        total_qty += qty
        
        # Save to list
        cart.append({"desc": desc, "qty": qty, "total": item_total})
        
        if input("Add more? (y/n): ").lower() == 'n':
            break

    print(f"\n[Raw Subtotal]: Rs. {grand_total:.2f}")

    #  CHALLENGES 27 & 28: Discounts 
    is_member = input("\nAre you a member? (y/n): ").lower()
    grand_total = logic.apply_discounts(grand_total, total_qty, is_member)

    #  CHALLENGE 29: Tax 
    tax_amt, rate = logic.calculate_tax(grand_total)
    grand_total += tax_amt
    print(f"[Tax] Rate {int(rate*100)}%:          +Rs. {tax_amt:.2f}")

    #  CHALLENGE 31: Payment 
    print("\nPayment: 1. Cash  2. Credit Card")
    if input("Select: ") == '2':
        surcharge = grand_total * config.CREDIT_CARD_SURCHARGE
        grand_total += surcharge
        print(f"[Surcharge] Card (2%):       +Rs. {surcharge:.2f}")

    #  CHALLENGE 32: Minimum Check 
    if grand_total < config.MIN_BILL_AMOUNT:
        print(f"\nERROR: Bill is Rs. {grand_total:.2f}. Minimum required is Rs. {config.MIN_BILL_AMOUNT}")
        return

    #  CHALLENGE 33: Loyalty & Final Bill 
    points = int(grand_total // 100)
    
    print("\n" + "*"*40)
    print(f"FINAL PAYABLE: Rs. {grand_total:.2f}")
    print(f"Loyalty Points: {points}")
    print("*"*40)

if __name__ == "__main__":
    main()
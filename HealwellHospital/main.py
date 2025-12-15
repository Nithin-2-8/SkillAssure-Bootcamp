"""
main.py

"""
import config
import logic

def display_menu():
    print("\n AVAILABLE SERVICES ")
    print(f"{'Code':<5} {'Service Name':<25} {'Price'}")
    print("-" * 45)
    
    # Loop through the arrays using index
    for i in range(len(config.SERVICE_CODES)):
        code = config.SERVICE_CODES[i]
        name = config.SERVICE_NAMES[i]
        price = config.SERVICE_PRICES[i]
        
        # Display logic
        price_str = str(price) if price > 0 else "Variable"
        print(f"{code:<5} {name:<25} {price_str}")
    print("-" * 45)

def main():
    print("=== HEALWELL HOSPITAL ===")
    
    # 1. Patient Info
    p_name = input("\nPatient Name: ")
    p_age = int(input("Age: "))
    
    # 2. Shopping Cart 
    cart_names = []
    cart_qtys = []
    cart_costs = []
    
    running_subtotal = 0.0

    while True:
        display_menu()
        
        try:
            code = int(input("\nEnter Service Code (0 to Finish): "))
        except ValueError:
            continue
            
        if code == 0:
            break
            
        # Find index in arrays
        index = logic.get_service_index(code)
        
        if index != -1:
            # Get details from arrays using index
            name = config.SERVICE_NAMES[index]
            base_price = config.SERVICE_PRICES[index]
            
            # Logic for Variable Prices (Pharmacy/Room)
            if code == 106: # Pharmacy
                cost = float(input(f"  Enter Amount for {name}: "))
                qty = 1
            elif code == 107: # Room Rent
                days = int(input(f"  Enter Number of Days for {name}: "))
                cost = base_price
                qty = days
            else:
                cost = base_price
                qty = 1
            
            line_total = cost * qty
            
            # Add to Cart Arrays
            cart_names.append(name)
            cart_qtys.append(qty)
            cart_costs.append(line_total)
            
            running_subtotal += line_total
            print(f"  -> Added: {name} | Total: Rs. {line_total}")
        else:
            print("Error: Invalid Code")

    if running_subtotal == 0:
        print("No services selected.")
        return

    # 3. Final Calculations
    print(f"\n[Subtotal]: Rs. {running_subtotal:.2f}")
    
    discount = logic.calculate_discount(running_subtotal, p_age)
    taxable = running_subtotal - discount
    tax = logic.calculate_tax(taxable)
    final_total = taxable + tax

    # 4. Print Invoice
    print("\n" + "="*50)
    print(f"INVOICE FOR: {p_name} (Age: {p_age})")
    print("="*50)
    print(f"{'Service':<25} {'Qty':<5} {'Cost':>10}")
    print("-" * 50)
    
    # Loop through Cart Arrays
    for i in range(len(cart_names)):
        print(f"{cart_names[i]:<25} {cart_qtys[i]:<5} {cart_costs[i]:>10.2f}")
        
    print("-" * 50)
    print(f"{'Subtotal':<30} Rs. {running_subtotal:>10.2f}")
    print(f"{'Discount':<30} Rs. -{discount:>10.2f}")
    print(f"{'Taxable Amount':<30} Rs. {taxable:>10.2f}")
    print(f"{'GST (18%)':<30} Rs. +{tax:>10.2f}")
    print("="*50)
    print(f"{'GRAND TOTAL':<30} Rs. {final_total:>10.2f}")
    print("="*50)

if __name__ == "__main__":
    main()
"""
Coding Challenge 3: Discount Calculator
Description: 
    This program calculates the discount amount and the final price to be paid
    based on a total bill amount and a discount percentage.

Formula: 
    Discount Amount = (Total Amount * Discount Percentage) / 100
    Final Payable = Total Amount - Discount Amount

Input:
    - Total Bill Amount (float)
    - Discount Percentage (float)
Output:
    - Discount Amount
    - Final Payable Amount
"""
def calculate_discount(total_amount,disc_pct):
    discount_value = (total_amount*disc_pct)/100
    final_value = total_amount-discount_value
    return discount_value,final_value
def main():
    print("Discount Calculator")
    try:
        #Take input
        total_amount=float(input("Enter the Total amount: "))
        disc_pct = float(input("Enter the Discount Percentage: "))
        #Check for negative Values
        if total_amount<0:
            print("Error:Invalid input.Toatal amaount should be positive")
            return
        if disc_pct<0 or disc_pct>100:
            print("Error:Invalid Input.Enter the correct Discount percentage")
            return
        #Calculate discount
        discount_amount,final_price = calculate_discount(total_amount,disc_pct)
        #Output
        print(f"\nBill Summary:")
        print(f"Total Amount:    Rs. {total_amount:.2f}")
        print(f"Discount ({disc_pct}%): - Rs. {discount_amount:.2f}")
        print(f"Grand Total:     Rs. {final_price:.2f}")
    
    except ValueError:
        print("Error : Invalid Entry")    

if __name__=="__main__":
    main()
    
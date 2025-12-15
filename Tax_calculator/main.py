"""
main.py

"""
# Import our custom modules
import config
import validators
import tax_logic

def main():
    print("\n GlobalNext Solutions: Tax Calculator ")
    
    #  1. INPUTS 
    while True:
        name = input("Enter Name: ").strip()
        if validators.validate_name(name): break
        print("Error: Name must be alphabets only and max 50 chars.")

    while True:
        emp_id = input("Enter EmpID: ").strip()
        if validators.validate_empid(emp_id): break
        print("Error: ID must be alphanumeric and 5-10 chars long.")

    basic = validators.get_valid_float("Enter Basic Monthly Salary: ")
    special = validators.get_valid_float("Enter Special Allowances: ")
    bonus_pct = validators.get_valid_float("Enter Bonus Percentage: ")

    # 2. CALCULATIONS 
    # Gross Salary
    gross_monthly = basic + special
    annual_base = gross_monthly * 12
    bonus_amt = annual_base * (bonus_pct / 100)
    annual_gross = annual_base + bonus_amt

    # Taxable Income (Using constant from config)
    if annual_gross > config.STANDARD_DEDUCTION:
        taxable_income = annual_gross - config.STANDARD_DEDUCTION
    else:
        taxable_income = 0.0

    # Tax & Cess (Using logic from tax_logic module)
    income_tax = tax_logic.calculate_tax(taxable_income)
    cess_amt = income_tax * config.CESS_PERCENTAGE
    total_tax = income_tax + cess_amt
    annual_net = annual_gross - total_tax

    # 3. REPORT     
    print(f"{'GlobalNext Solutions - TAX REPORT':^50}")    
    print(f"{'Field':<25} | {'Details':>20}")
    print("-" * 50)
    print(f"{'Name':<25} | {name:>20}")
    print(f"{'Annual Gross':<25} | {annual_gross:>20,.2f}")
    print(f"{'Taxable Income':<25} | {taxable_income:>20,.2f}")
    print(f"{'Total Tax':<25} | {total_tax:>20,.2f}")
    print(f"{'Net Salary':<25} | {annual_net:>20,.2f}")
    

if __name__ == "__main__":
    main()
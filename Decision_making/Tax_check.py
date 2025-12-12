"""
Challenge 7: Salary & Tax Eligibility Check
Rule: Salary > 3,00,000 must pay tax.
"""
def main():
    name = input("Enter Employee Name: ")
    salary_str = input("Enter Annual Salary in Rs: ")
    
    try:
        salary = float(salary_str)
        
        print(f"\nChecking tax status for {name}...")
     
    
        if salary > 300000:
            print("Result: You must pay tax.")
        else:
            print("Result: You are NOT required to pay tax.")
            
    except ValueError:
        print("Invalid salary input.")

if __name__ == "__main__":
    main()
"""
validators.py
Handles input validation logic.
"""

def validate_name(name):
    #Checks if name is non-empty, max 50 chars, alphabets only
    if not name: return False
    if len(name) > 50: return False
    if name.replace(" ", "").isalpha(): return True
    return False

def validate_empid(emp_id):
    #Checks if ID is 5-10 chars and alphanumeric.
    if len(emp_id) < 5 or len(emp_id) > 10: return False
    if emp_id.isalnum(): return True
    return False

def get_valid_float(prompt, min_val=0.0):
    #Safe input function for money/percentages.
    while True:
        try:
            value = float(input(prompt))
            if value >= min_val:
                return value
            else:
                print(f"Error: Value must be at least {min_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
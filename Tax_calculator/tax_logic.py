"""
tax_logic.py
Core calculation engine 
"""

def calculate_tax(taxable_income):
    # 1. Section 87A Rebate Logic
    if taxable_income <= 700000:
        return 0.0

    # 2. Progressive Slabs 
    tax = 0.0
    
    if taxable_income <= 300000:
        tax = 0.0
        
    elif taxable_income <= 600000:
        # Tax on income exceeding 3L
        tax = (taxable_income - 300000) * 0.05
        
    elif taxable_income <= 900000:
        # 15k (from prev slab) + 10% of remainder
        tax = 15000 + (taxable_income - 600000) * 0.10
        
    elif taxable_income <= 1200000:
        # 45k (from prev slabs) + 15% of remainder
        tax = 45000 + (taxable_income - 900000) * 0.15
        
    elif taxable_income <= 1500000:
        # 90k (from prev slabs) + 20% of remainder
        tax = 90000 + (taxable_income - 1200000) * 0.20
        
    else:
        # 1.5L (from prev slabs) + 30% of remainder
        tax = 150000 + (taxable_income - 1500000) * 0.30
        
    return tax
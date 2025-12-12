"""
Coding Challenge 5: Farmer Problem Statement

Description: 
    Calculates the overall sales and chemical-free farming realization for 
    Mahesh (the farmer) based on crop yields, land area, and conversion timelines.

Timeline Logic for Chemical-Free:
    - Vegetables (Tomato, Potato, Cabbage): Ready after 6 months.
    - Sunflower: Ready after 6 + 4 = 10 months.
    - Sugarcane: Ready after 10 + 4 = 14 months.
    
    * Requirement: "Sales realization at 11 months". 
      This implies Sugarcane is NOT included in the chemical-free total.
"""

def calculate_crop_sales(acres, yield_per_acre, price_per_unit, is_price_per_tonne=False):
    
    total_yield_tonnes = acres * yield_per_acre
    
    if is_price_per_tonne:
        # Direct calculation: Tonnes * Price/Tonne
        total_sales = total_yield_tonnes * price_per_unit
    else:
        # Conversion needed: Tonnes -> Kg (* 1000) then multiply by Price/Kg
        total_yield_kg = total_yield_tonnes * 1000
        total_sales = total_yield_kg * price_per_unit
        
    return total_sales

def main():
    print(" Farmer Sales Calculator ")
    
    
    # --- CONSTANTS ---
    TOTAL_LAND = 80
    SEGMENTS = 5
    ACRES_PER_SEGMENT = TOTAL_LAND / SEGMENTS 

    # 1. TOMATO CALCULATION (Complex Yield)
    # 30% of land -> 10 tonne/acre
    # 70% of land -> 12 tonne/acre
    tomato_land_1 = ACRES_PER_SEGMENT * 0.30
    tomato_land_2 = ACRES_PER_SEGMENT * 0.70
    
    sales_tomato_1 = calculate_crop_sales(tomato_land_1, 10, 7) 
    sales_tomato_2 = calculate_crop_sales(tomato_land_2, 12, 7)
    total_tomato_sales = sales_tomato_1 + sales_tomato_2
    print(f"Total Tomato Sales:    Rs. {total_tomato_sales:,.2f}")

    # 2. POTATO CALCULATION
    # 10 tonne/acre, Rs. 20/kg
    total_potato_sales = calculate_crop_sales(ACRES_PER_SEGMENT, 10, 20)
    print(f"Total Potato Sales:    Rs. {total_potato_sales:,.2f}")

    #3. CABBAGE CALCULATION
    # 14 tonne/acre, Rs. 24/kg
    total_cabbage_sales = calculate_crop_sales(ACRES_PER_SEGMENT, 14, 24)
    print(f"Total Cabbage Sales:   Rs. {total_cabbage_sales:,.2f}")

    #4. SUNFLOWER CALCULATION
    # 0.7 tonne/acre, Rs. 200/kg
    total_sunflower_sales = calculate_crop_sales(ACRES_PER_SEGMENT, 0.7, 200)
    print(f"Total Sunflower Sales: Rs. {total_sunflower_sales:,.2f}")

    #5. SUGARCANE CALCULATION 
    # 45 tonne/acre, Rs. 4000/TONNE (Note the True flag)
    total_sugarcane_sales = calculate_crop_sales(ACRES_PER_SEGMENT, 45, 4000, is_price_per_tonne=True)
    print(f"Total Sugarcane Sales: Rs. {total_sugarcane_sales:,.2f}")

    

    # CALCULATIONS 
    overall_sales = (total_tomato_sales + total_potato_sales + 
                     total_cabbage_sales + total_sunflower_sales + 
                     total_sugarcane_sales)
    
    # Chemical Free Sales at Month 11
    # Only Veggies (Month 6) + Sunflower (Month 10) are ready.
    # Sugarcane (Month 14) is excluded.
    chem_free_sales_11_months = (total_tomato_sales + total_potato_sales + 
                                 total_cabbage_sales + total_sunflower_sales)

    # Output
    print(f"1. OVERALL SALES (All Crops):           Rs. {overall_sales:,.2f}")
    print(f"2. SALES AT 11 MONTHS (Excl Sugarcane): Rs. {chem_free_sales_11_months:,.2f}")
    

if __name__ == "__main__":
    main()
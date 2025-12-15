"""
config.py
Stores hospital data in simple Arrays .
"""

# 1. Service Codes
SERVICE_CODES = [101, 102, 103, 104, 105, 106, 107]

# 2. Service Names (Must match order of CODES)
SERVICE_NAMES = [
    "General Consultation",
    "Specialist Consult",
    "Blood Test (CBC)",
    "X-Ray",
    "MRI Scan",
    "Pharmacy / Meds",
    "Room Rent (Per Day)"
]

# 3. Service Prices (Must match order of CODES)
# 0.0 means the price is variable (entered by user)
SERVICE_PRICES = [500.0, 1000.0, 300.0, 800.0, 5000.0, 0.0, 2000.0]

# Rules
GST_RATE = 0.18
SENIOR_AGE_LIMIT = 60
SENIOR_DISCOUNT = 0.20
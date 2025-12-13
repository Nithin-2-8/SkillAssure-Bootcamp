"""
Challenge 10: Student Report Card Problem
Requirements:
1. Accept Student Name and 3 Subject Scores.
2. Calculate Total and Average.
3. Determine Class based on Average:
   - 1st Class: >= 60
   - 2nd Class: >= 50 
   - Pass Class: >= 35
   - Fail: < 35 
"""

def get_valid_score(subject_name):
    while True:
        try:
            score = float(input(f"Enter score for {subject_name}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("--- Student Report Card System ---")
    
    #  Input Validation for Name 
    while True:
        name = input("Enter Student Name: ").strip()
        if name and name.replace(" ", "").isalpha():
            break
        print("Error: Name must contain only alphabets.")

    #  Input Scores
    s1 = get_valid_score("Subject 1")
    s2 = get_valid_score("Subject 2")
    s3 = get_valid_score("Subject 3")

    # Calculations
    total_score = s1 + s2 + s3
    average_score = total_score / 3

    # Determine Class 
    
    if average_score >= 60:
        result_class = "1st Class"
    elif average_score >= 50:
        result_class = "2nd Class"
    elif average_score >= 35:
        result_class = "Pass Class"
    else:
        result_class = "Fail"

    #  Display Report
    print("\n" + "="*30)
    print(f"REPORT CARD: {name.upper()}")
    print(f"Subject 1:   {s1}")
    print(f"Subject 2:   {s2}")
    print(f"Subject 3:   {s3}")
    print("-" * 30)
    print(f"TOTAL:       {total_score}")
    print(f"AVERAGE:     {average_score:.2f}")
    print("-" * 30)
    print(f"RESULT:      {result_class}")
    

if __name__ == "__main__":
    main()
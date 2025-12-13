"""
Challenge 19: Display the Series 4, 16, 36, 64...
"""
def main():
    n = int(input("How many terms (N)? "))
    
    for i in range(1, n + 1):
        # Calculate even number: 2 * i
        even_num = 2 * i
        # Square it
        term = even_num ** 2
        
        print(term, end=" ")
    print()

if __name__ == "__main__":
    main()
"""
Challenge 18: Display the Series 1, 3, 5, 7... N
"""
def main():
    n = int(input("Enter value of N: "))
    # Start at 1, go up to N, increment by 2
    for i in range(1, n + 1, 2):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
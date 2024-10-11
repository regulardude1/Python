def factorial_iterative(n_iterative):
    result = 1
    for i in range(2, n_iterative + 1):
        result *= i
    return result

def factorial_recursive(n_recursive):
    if n_recursive == 0 or n_recursive == 1:
        return 1
    else:
        return n_recursive * factorial_recursive(n_recursive - 1)

def get_valid_number():
    while True:
        try:
            n = int(input("Please input a non-negative integer to calculate its factorial: "))
            if n < 0:
                print("The number must be non-negative. Try again.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_method():
    while True:
        method = input("Which method would you like to use? (Type 'iterative' or 'recursive'): ").lower()
        if method in ["iterative", "recursive"]:
            return method
        else:
            print("Invalid choice. Please type either 'iterative' or 'recursive'.")

if __name__ == "__main__":
    # Get the user's choice of method and number
    method = get_valid_method()
    n = get_valid_number()

    # Perform the calculation 
    if method == "iterative":
        print(f"Iterative: {n}! = {factorial_iterative(n)}")
    else:
        print(f"Recursive: {n}! = {factorial_recursive(n)}")

#This program calculates the factorial of a non-negative integer using either an iterative or recursive method based on the user's choice.
#It includes input validation and exception handling to ensure proper user input and computation.



def factorial_iterative(n_iterative):
    try:
        result = 1
        if n_iterative < 0:
            raise ValueError("Input must be a non-negative integer.")
        for i in range(2, n_iterative + 1):
            result *= i
        return result
    except Exception as e:
        print(f"Error in iterative calculation: {e}")
        return None

def factorial_recursive(n_recursive):
    try:
        if n_recursive < 0:
            raise ValueError("Input must be a non-negative integer.")
        if n_recursive == 0 or n_recursive == 1:
            return 1
        else:
            return n_recursive * factorial_recursive(n_recursive - 1)
    except Exception as e:
        print(f"Error in recursive calculation: {e}")
        return None

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
        result = factorial_iterative(n)
        if result is not None:
            print(f"Iterative: {n}! = {result}")
    else:
        result = factorial_recursive(n)
        if result is not None:
            print(f"Recursive: {n}! = {result}")

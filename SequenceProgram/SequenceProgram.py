# This program generates a sequence of numbers and asks the user to guess the sixth term of the sequence.
# The user can choose between four types of sequences: arithmetic, geometric, Fibonacci, and square numbers.



import random

print("Welcome to the Sequence Program!\nPlease select a sequence to generate:\n1. Arithmetic Sequence\n2. Geometric Sequence\n3. Fibonacci Sequence\n4. Square Numbers")

def arithmetic_sequence(a, d):
    return [a + i * d for i in range(6)]

def geometric_sequence(a, r):
    return [a * (r ** i) for i in range(6)]

def fibonacci_sequence():
    sequence = [0, 1]
    for i in range(4):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def square_numbers():
    return [i ** 2 for i in range(6)]

def get_valid_sequence_choice():
    while True:
        try:
            user_input = int(input("Enter the number of the sequence you would like to generate: "))
            if user_input not in [1, 2, 3, 4]:
                raise ValueError("Invalid choice. Please select a number between 1 and 4.")
            return user_input
        except ValueError as e:
            print(e)

def get_valid_guess():
    while True:
        try:
            user_guess = int(input("What is the sixth term? "))
            return user_guess
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    sequences = [
        ("Arithmetic Sequence", arithmetic_sequence(2, 3)),  
        ("Geometric Sequence", geometric_sequence(3, 2)),   
        ("Fibonacci Sequence", fibonacci_sequence()),        
        ("Square Numbers", square_numbers())                 
    ]

    # Get the user's choice of sequence
    user_choice = get_valid_sequence_choice()

    # Select the chosen sequence
    sequence_name, sequence = sequences[user_choice - 1]

    print(f"Sequence Type: {sequence_name}")
    print("The first five terms are:", sequence[:5])

    # Get the user's guess for the sixth term
    user_guess = get_valid_guess()

    # Check if the guess is correct
    if user_guess == sequence[5]:
        print("Correct! Well done.")
    else:
        print(f"Wrong. The correct sixth term was {sequence[5]}.")

if __name__ == "__main__":
    main()

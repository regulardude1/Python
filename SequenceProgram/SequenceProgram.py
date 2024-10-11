import random

print("Welcome to the Sequence Program!\nPlease select a sequence to generate:\n1. Arithmetic Sequence\n2. Geometric Sequence\n3. Fibonacci Sequence\n4. Square Numbers")
user_input = input("Enter the number of the sequence you would like to generate: ")

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

def main():
    sequences = [
        ("Arithmetic Sequence", arithmetic_sequence(2, 3)),  
        ("Geometric Sequence", geometric_sequence(3, 2)),   
        ("Fibonacci Sequence", fibonacci_sequence()),        
        ("Square Numbers", square_numbers())                 
    ]

    # Select a random sequence
    sequence_name, sequence = random.choice(sequences)


    print(f"Sequence Type: {sequence_name}")
    print("The first five terms are:", sequence[:5])


    user_guess = int(input("What is the sixth term? "))

    # Check if the guess is correct
    if user_guess == sequence[5]:
        print("Correct! Well done.")
    else:
        print(f"Wrong. The correct sixth term was {sequence[5]}.")

if __name__ == "__main__":
    main()


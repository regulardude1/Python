#This program helps find the number of ways to choose a certain number of cookies from a certain number of types of cookies.


import math

def cookie_combinations(total, types):
   
    return math.comb(total + types - 1, types - 1)


def ask_user():
    total = int(input("How many cookies do you have? "))  
    types = int(input("How many types of cookies do you have? "))  
    return total, types


def calculate_and_display_combinations(total, types):
    ways = cookie_combinations(total, types)
    print(f"The number of different ways to choose {total} cookies from {types} kinds is: {ways}")

if __name__ == "__main__":
    total, types = ask_user()  # Get user input
    calculate_and_display_combinations(total, types)  # Calculate and display the result
              
#This program calculates the number of people needed in a room to have a certain probability of two people sharing a birthday.
#The program uses the birthday paradox to calculate the number of people needed to have a certain probability of two people sharing a birthday.


import math

def birthday_paradox(thresholds):
    days_in_year = 365
    probabilities = []  # To store the number of people for each threshold

    for threshold in thresholds:
        num_people = 0
        prob_no_shared_birthday = 1  # Probability that two people wont share a birthday

        while (1 - prob_no_shared_birthday) < threshold:
            num_people += 1
            prob_no_shared_birthday *= (days_in_year - num_people + 1) / days_in_year

        probabilities.append(num_people)

    return probabilities

def main():
    # % probabilities
    thresholds = [0.70, 0.80, 0.90, 0.95, 0.99]

    results = birthday_paradox(thresholds)

    for i, threshold in enumerate(thresholds):
        print(f"To have at least {int(threshold * 100)}% probability, you need {results[i]} people.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Nov 27, 2023
# Simulates rolling two dice until doubles are obtained,
# calculates the percentage chance of rolling doubles and
# the average number of rolls across multiple test cases,
# using the built-in random module.

import random


def simulate_dice_rolls():
    # initializing variables
    total_rolls = 0
    successful_runs = 0
    test_cases = 3  # Number of times to run the simulation

    # for loop for the amount of test cases
    for test_case in range(1, test_cases + 1):
        print(f"\nTest Case {test_case}:")

        rolls = 0

        # while true for the continuous dice rolls
        while True:
            # Simulate rolling 2 dice
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            # Display the roll
            print(f"Roll {rolls + 1}: {dice1}  {dice2}")

            # Check for doubles
            if dice1 == dice2:
                if rolls == 0:
                    print(f"Doubles obtained in the first roll!\n")
                else:
                    print(f"Doubles obtained in {rolls + 1} rolls!\n")
                successful_runs += 1
                break  # Exit the loop when doubles are obtained

            rolls += 1

        total_rolls += rolls

    # Calculate and display the percentage chance and average rolls
    percentage_chance = (successful_runs / test_cases) * 100
    average_rolls = total_rolls / test_cases
    print(f"Percentage chance of rolling doubles: {percentage_chance}%")
    print(f"Average number of rolls: {average_rolls}")


if __name__ == "__main__":
    simulate_dice_rolls()


# Name: Amaney Ibrahim
# Course: CMP131
# Week: 08
# Lab: 01
# Assignment: Increasing and Decreasing Loop Patterns
# Date: 11/12/26

# program title
print("============== ~ Increasing and Decreasing Loop Patterns ~ ==============")

# Pattern A: Increasing plus signs
print()
print("Pattern A: Increasing")

# Outer loop controls the rows
for row in range(1, 11):

    # Inner loop prints the plus signs
    for column in range(row):
        print("+", end="")

    # Move to the next row
    print()

# Pattern B: Decreasing plus signs
print()
print("Pattern B: Decreasing")

# Outer loop controls the rows
for row in range(10, 0, -1):

    # Inner loop prints the plus signs
    for column in range(row):
        print("+", end="")

    # Move to the next row
    print()

# Final output
print()
print("End of Loop Patterns")

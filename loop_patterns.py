
# Name: Amaney Ibrahim
# Course: CMP131
# Week: 08
# Lab: 01
# Assignment: Sales Bar Chart
# Date: 11/12/26

# Title
print("=========== ~ Sales Bar Chart for Five Stores ~ ===========")

# Initialize sales variables
sales1 = 0
sales2 = 0
sales3 = 0
sales4 = 0
sales5 = 0

# Ask for sales from each store
for store in range(1, 6):
    sales = float(input("Enter today's sales for Store " + str(store) + ": $"))

    # Validating sales input
    while sales < 0:
        print("Error: Sales cannot be negative.")
        sales = float(input("Enter today's sales again: $"))

    # Storing each sales amount
    if store == 1:
        sales1 = sales
    elif store == 2:
        sales2 = sales
    elif store == 3:
        sales3 = sales
    elif store == 4:
        sales4 = sales
    else:
        sales5 = sales

# chart heading
print()
print(" =========== ~ SALES BAR CHART ~ ===========")
print("Each * represents $100")

# sales bars for all five stores
for store in range(1, 6):

    # Select the sales amount
    if store == 1:
        sales = sales1
    elif store == 2:
        sales = sales2
    elif store == 3:
        sales = sales3
    elif store == 4:
        sales = sales4
    else:
        sales = sales5

    # Convert sales to asterisks
    asterisks = int(sales // 100)

    # Display store label
    print("Store", store, ": ", end="")

    # Print asterisks using a loop
    for count in range(asterisks):
        print("*", end="")

    # Move to the next line
    print()

# Final output
print()
print("End of Sales Bar Chart")

# Barakat Owoalade
# March 16, 2026

# Problem 3: Using a while loop, ask the user to enter numbers.
# Each number entered will be added to a list and summed together.
# The loop stops when the total sum becomes greater than 100.

# Create an empty list
numbers = []

# Start the sum at 0
total = 0

# Continue the loop while the total is less than or equal to 100
while total <= 100:

    # Ask the user to enter a number
    num = int(input("Enter a number: "))

    # Add the number to the list
    numbers.append(num)

    # Add the number to the total
    total = total + num

# Print the list of numbers entered
print("Numbers entered:", numbers)

# Print the total sum
print("Total sum:", total)

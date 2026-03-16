# Barakat Owoalade
# March 16, 2026

# Problem 2: Using a while loop, create a list called L that contains the numbers 0 to 10.
# Each loop adds the current counter value to the list and then increases the counter by 1.

# Create an empty list
L = []

# Start the counter at 0
counter = 0

# Run the loop while the counter is less than or equal to 10
while counter <= 10:
    
    # Add the counter value to the list
    L.append(counter)
    
    # Increase the counter by 1
    counter = counter + 1

# Print the list to confirm the result
print(L)

# Barakat Owoalade
# March 16, 2026

# Problem 4: Create a while loop that starts a counter at 0 and runs until 50.
# If the counter is divisible by 10, add it to a list called tens.

# Create an empty list called tens
tens = []

# Start the counter at 0
counter = 0

# Run the loop while the counter is less than or equal to 50
while counter <= 50:

    # Check if the counter is divisible by 10
    if counter % 10 == 0:
        tens.append(counter)

    # Increase the counter by 1
    counter = counter + 1

# Print the list to confirm the results
print(tens)

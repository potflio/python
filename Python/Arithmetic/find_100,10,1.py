# Get number input from the user
num = int(input("Enter a number: "))

# Extract 100s, 10s, and 1s
hundreds = (num // 100) % 10
tens = (num // 10) % 10
ones = num % 10

# Print the results
print("100s digit:", hundreds)
print("10s digit:", tens)
print("1s digit:", ones)

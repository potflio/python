numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the sum
total = sum(numbers)

# Output the result
print("Sum of the 5 numbers is:", total)

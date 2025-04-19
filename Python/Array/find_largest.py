# Input 5 numbers
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find the largest number
largest = max(numbers)

# Output result
print("Largest number is:", largest)

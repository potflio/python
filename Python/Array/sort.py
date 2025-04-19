# Input 5 numbers
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Sort the list
numbers.sort()

# Output sorted list
print("Sorted numbers:", numbers)

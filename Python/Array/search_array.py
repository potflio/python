# Input 5 numbers
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Ask for number to search
search = int(input("Enter the number to search: "))

# Check and display result
if search in numbers:
    print(f"{search} found at index {numbers.index(search)}")
else:
    print(f"{search} is not found in the array")

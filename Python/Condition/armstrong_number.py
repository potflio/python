# Get input from user
num = int(input("Enter a number: "))

# Convert number to string to get the number of digits
num_str = str(num)
n = len(num_str)

# Calculate sum of digits raised to power n
armstrong_sum = sum(int(digit) ** n for digit in num_str)

# Check if it's an Armstrong number
if armstrong_sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")

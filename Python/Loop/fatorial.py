# Get input from user
num = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Check if the number is negative, zero or positive
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is:", factorial)

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Compare and find the largest
if num1 > num2:
    print("The largest number is:", num1)
elif num2 > num1:
    print("The largest number is:", num2)
else:
    print("Both numbers are equal.")

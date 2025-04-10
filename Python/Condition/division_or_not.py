# Get two numbers from the user
num = int(input("Enter the number: "))
divisor = int(input("Enter the divisor: "))

# Check divisibility
if num % divisor == 0:
    print(num, "is divisible by", divisor)
else:
    print(num, "is NOT divisible by", divisor)

# Get input from the user
num = int(input("Enter a number: "))

# Find and print factors
print("Factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    power = 1
    for j in range(i):
        power *= i
    total += power

print("Sum of powers from 1^1 to", n, "^", n, "is:", total)

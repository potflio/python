n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    total += fact

print("Sum of factorials from 1! to", n, "is:", total)

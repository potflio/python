# Create empty 2x2 matrix
matrix = []

# Input values row by row
for i in range(2):
    row = []
    for j in range(2):
        val = int(input(f"Enter value at position ({i},{j}): "))
        row.append(val)
    matrix.append(row)

# Print matrix
print("2x2 Matrix:")
for row in matrix:
    print(row)

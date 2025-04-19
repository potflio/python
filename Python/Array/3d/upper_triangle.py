# Input 3x3 matrix
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        val = int(input(f"Enter value at ({i},{j}): "))
        row.append(val)
    matrix.append(row)

# Print upper triangle
print("Upper Triangle Matrix:")
for i in range(3):
    for j in range(3):
        if i <= j:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

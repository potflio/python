# Step 1: Initialize an empty list to hold the 4x4 matrix
matrix = []

# Step 2: Take input for each element in the 4x4 matrix
print("Enter values for a 4x4 matrix:")

for i in range(4):  # Loop for each row
    row = []  # Temporary list to store one row
    for j in range(4):  # Loop for each column
        val = int(input(f"Enter value at position ({i},{j}): "))  # Input from user
        row.append(val)  # Add value to the current row
    matrix.append(row)  # Add completed row to the matrix

# At this point, 'matrix' contains the full 4x4 grid

# Step 3: Calculate the sum of the **primary diagonal**
# Primary diagonal elements are at positions (0,0), (1,1), (2,2), (3,3)
primary_diag = 0
for i in range(4):
    primary_diag += matrix[i][i]

# Step 4: Calculate the sum of the **secondary diagonal**
# Secondary diagonal elements are at positions (0,3), (1,2), (2,1), (3,0)
secondary_diag = 0
for i in range(4):
    secondary_diag += matrix[i][3 - i]

# Step 5: Total diagonal sum
total = primary_diag + secondary_diag

# Step 6: Display the matrix and the sum
print("\nThe 4x4 Matrix is:")
for row in matrix:
    print(row)

print("\nSum of primary diagonal:", primary_diag)
print("Sum of secondary diagonal:", secondary_diag)
print("Total sum of diagonals:", total)

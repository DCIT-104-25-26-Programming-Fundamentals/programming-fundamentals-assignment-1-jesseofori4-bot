# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols):
    """Reads a matrix of size rows x cols from user input."""
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                row = list(map(int, row_input.split()))
                if len(row) != cols:
                    raise ValueError(f"Row must have exactly {cols} values.")
                matrix.append(row)
                break
            except ValueError as e:
                print(e)
    return matrix
def print_matrix(matrix):
    """Prints the matrix in a neat, aligned grid format."""
    for row in matrix:
        print(" ".join(f"{val:>5}" for val in row))

def transpose_matrix(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(matrix_a, matrix_b):
    """Adds two matrices of the same size."""
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must be of the same size for addition.")
    result = []
    for i in range(len(matrix_a)):
        new_row = []
        for j in range(len(matrix_a[0])):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result
def multiply_matrices(matrix_a, matrix_b):
    """Multiplies two matrices (matrix_a of size M x N and matrix_b of size N x P)."""
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in A must equal number of rows in B for multiplication.")
    result = []
    for i in range(len(matrix_a)):
        new_row = []
        for j in range(len(matrix_b[0])):
            sum_product = 0
            for k in range(len(matrix_b)):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(sum_product)
        result.append(new_row)
    return result
if __name__ == "__main__":
    # Part A: Transpose a Matrix
    print("PART A — Transpose a Matrix")
    rows_a = int(input("Enter number of rows for matrix A: "))
    cols_a = int(input("Enter number of columns for matrix A: "))
    matrix_a = read_matrix(rows_a, cols_a)
    print("Original Matrix A:")
    print_matrix(matrix_a)
    transposed_a = transpose_matrix(matrix_a)
    print("Transposed Matrix A:")
    print_matrix(transposed_a)

    print("\nPART B — Add Two Matrices")
    rows_b = int(input("Enter number of rows for matrix B: "))
    cols_b = int(input("Enter number of columns for matrix B: "))
    matrix_b = read_matrix(rows_b, cols_b)
    print("Original Matrix B:")
    print_matrix(matrix_b)
    try:
        result_add = add_matrices(matrix_a, matrix_b)
        print("Sum of Matrices A and B:")
        print_matrix(result_add)
    except ValueError as e:
        print(e)

    print("\nPART C — Multiply Two Matrices")
    rows_b = int(input("Enter number of rows for matrix B: "))
    cols_b = int(input("Enter number of columns for matrix B: "))
    matrix_b = read_matrix(rows_b, cols_b)
    print("Original Matrix B:")
    print_matrix(matrix_b)
    try:
        result_multiply = multiply_matrices(matrix_a, matrix_b)
        print("Product of Matrices A and B:")
        print_matrix(result_multiply)
    except ValueError as e:
        print(e)
        if cols_a != rows_b:
            print(f"Cannot multiply: Number of columns in A ({cols_a}) must equal number of rows in B ({rows_b}).")
        else:
            print("Matrix A:")
            matrix_a = read_matrix(rows_a, cols_a, "matrix A")
            print("Matrix B:")
            matrix_b = read_matrix(rows_b, cols_b, "matrix B")
            print("\nmatrix product of A and B:")
            print_matrix(multiply_matrices(matrix_a, matrix_b))
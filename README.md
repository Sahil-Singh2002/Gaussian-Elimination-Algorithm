# Gaussian Elimination Algorithm

This repository contains a Python implementation of the Gaussian Elimination algorithm using elementary row operations.

## Description

The Gaussian Elimination algorithm is a numerical method for solving systems of linear equations and finding the row echelon form of a matrix. It operates by performing a sequence of row operations to reduce the given matrix to an upper triangular form, making it easier to solve the system of equations.

The algorithm follows these steps:

1. Iterate over each column in the matrix.
2. For each column, find the maximum absolute value below the diagonal and swap the current row with the row containing the maximum value, if it is larger than the diagonal element.
3. Use elementary row operations to eliminate values below the diagonal in the current column, making them zero.
4. Repeat steps 2 and 3 for the remaining columns.
5. The resulting matrix will be in row echelon form, ready for further analysis or solving the system of equations.

## Usage

To use the Gaussian Elimination algorithm, follow these steps:

1. Install the required dependencies, including NumPy.
2. Import the necessary functions from the provided module: `find_max_column_value`, `swap_rows`, `swap_cols`, and `add_row`.
3. Call the `Gauss_elimination` function with the input matrix as an argument.
4. The function will return the modified matrix after applying Gaussian Elimination.

```python
import numpy as np
from gaussian_elimination import Gauss_elimination

# Create a matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Apply Gaussian Elimination
result = Gauss_elimination(A)
print(result)

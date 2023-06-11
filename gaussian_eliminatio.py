import numpy as np

def find_max_column_value(A, i, j):
    """
    Find the entry in column j with maximum absolute value amongst rows i, i+1, ..., r.

    Parameters:
        A (ndarray): Input matrix.
        i (int): Starting row index.
        j (int): Column index.

    Returns:
        Tuple: (max_value, max_index), where max_value is the maximum absolute value and max_index is the row index.

    Raises:
        IndexError: If i is not a valid row index or j is not a valid column index.
    """
    if i < 0 or i >= A.shape[0]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[1]:
        raise IndexError(f"Index j={j} out of bounds!")

    Z = A[i:, j]
    absolute_vals = np.abs(Z)
    maximum = np.max(absolute_vals)
    max_index = np.argmax(absolute_vals) + i

    return maximum, max_index


def swap_rows(A, i, j):
    """
    Swap rows i and j in the input matrix A and return the modified matrix.

    Parameters:
        A (ndarray): Input matrix.
        i (int): First row index.
        j (int): Second row index.

    Returns:
        ndarray: Matrix A with rows i and j swapped.

    Raises:
        IndexError: If i or j is not a valid row index.
    """
    if i < 0 or i >= A.shape[0]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[0]:
        raise IndexError(f"Index j={j} out of bounds!")

    B = np.copy(A)
    B[[i, j], :] = B[[j, i], :]

    return B


def swap_cols(A, i, j):
    """
    Swap columns i and j in the input matrix A and return the modified matrix.

    Parameters:
        A (ndarray): Input matrix.
        i (int): First column index.
        j (int): Second column index.

    Returns:
        ndarray: Matrix A with columns i and j swapped.

    Raises:
        IndexError: If i or j is not a valid column index.
    """
    if i < 0 or i >= A.shape[1]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[1]:
        raise IndexError(f"Index j={j} out of bounds!")

    B = np.copy(A)
    B[:, [i, j]] = B[:, [j, i]]

    return B


def add_row(A, i, j, a):
    """
    Replace row i of the input matrix A with row i plus a times row j and return the modified matrix.

    Parameters:
        A (ndarray): Input matrix.
        i (int): Row index to replace.
        j (int): Row index to multiply by a.
        a (float): Scalar multiplier.

    Returns:
        ndarray: Matrix A with row i replaced by row i plus a times row j.

    Raises:
        IndexError: If i or j is not a valid row index.
    """
    if i < 0 or i >= A.shape[0]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[0]:
        raise IndexError(f"Index j={j} out of bounds!")

    B = np.copy(A

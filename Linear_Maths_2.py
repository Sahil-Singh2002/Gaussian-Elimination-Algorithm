import numpy as np
def find_max_column_value(A,i,j):
    # Your code here, i is the number of rows and j is the number of coloumbs
    if i < 0 or i >= A.shape[0]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[1]:
        raise IndexError(f"Index j={j} out of bounds!")
    # slice of the matrix from row i onwards and coloumn j.
    Z=A[i:,j] 
    absolute_vals = []
    # itterate through z
    for k in range(len(Z)):
        absolute_vals.append(abs(Z[k]))
    maximum = 0
    #itterating throuigh absoloute values
    for each in absolute_vals:
        if each > maximum:
            maximum = each
    return (maximum,absolute_vals.index(maximum) + i)

def swap_rows(A,i,j):
    # Your code here
    if i < 0 or i >= A.shape[0]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[0]:
        raise IndexError(f"Index j={j} out of bounds!")
    B = A.copy()
    B[[i,j]] = B[[j,i]]  
    return B
 
def swap_cols(A,i,j):
    # Your code here
    if i < 0 or i >= A.shape[1]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[1]:
        raise IndexError(f"Index j={j} out of bounds!")
    B = A.copy()
    B[:,[i,j]] = B[:,[j,i]]  
    return B

def add_row(A,i,j,a):
    if i < 0 or i >= A.shape[0]:
        raise IndexError(f"Index i={i} out of bounds!")
    if j < 0 or j >= A.shape[0]:
        raise IndexError(f"Index i={j} out of bounds!")
    B = A.copy()
    B[i] = A[i] + a*A[j]
    return B

def Gauss_elimination(A):
    if A.dtype  != 'float64':
            raise TypeError("Need a matrix with float64 entries!")
        #raises type error if data type is wrong
    for j in range(min(A.shape)-1):
        max_value= find_max_column_value(A,j+1,j)
        #will find the greatest value in coloumn j
        if max_value[0] == 0:
            continue
        #if the max value is 0 then we just skip
        if max_value[0]> abs(A[j,j]):
            A = swap_rows(A,j,max_value[1])
        #if the max value is greater then the diagonal value then swap the rows, the abs() makes sure that if a value on the diagonal and is negative, it will get swapped that way. otherwise it wont.
        for i in range(j+1,A.shape[0]):
            A = add_row(A,i,j,-1*(A[i,j]/A[j,j]))
        #basicaly makes each element under the diagonal = to 0    
            if abs(A[i,j])< min(A.shape)*np.finfo('float32').eps:
                A[i,j] == 0 
    return A

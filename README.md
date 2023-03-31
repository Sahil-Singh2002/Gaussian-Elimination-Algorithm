# Linear Maths 2

These set of codes are used in the Gausian elimanation algorithm for matrix of dimension (*n* x *n*). The set of codes include find_max_column_value, swap_row, swap_column and Gauss_elimination which uses the functions above to exacute this command.

* The function find_max_column_value(A,i,j) with parameters, A is the matrix given as a 2-dimensional NumPy-array, i,j both positive integers. This returns the entry in column j with maximum absoolute value amongst rows i,i+1,... together with its row index.   

* The function swap_rows(A,i,j) and swap_columns(A,i,j) both take matrix A as an input and two postive integers i and j. They both return a copy of the matrix A where the rows i and j, or columns i and j, are swapped respectively.

* The function Gauss_elimination(A) takes matrix A as an input, uses the previous functions and an additional function add_row to implememnt the Gaussian Elimination algorithm using elementary row operations. We assume A = (*a*_mn) is an *r X k* matrix given by a 2-dimensional NumPy array with entries of type float64. Then the Gauss Elimination algorithm can be written as
  - Iterate over each column in turn.
  - For each column, j, find the maximum absolute value below the diagonal and if larger than the diagonal value then swap the current row for the row corresponding to the maximum.
  - If the maximum value is 0 continue with next column.
  - Otherwise use elementary row operations to eliminate values in the current column from from all rows below the diagonal.
  - Once we have reached the end of the columns, return the current matrix. 
  - Note that if there are more columns than rows you can stop after "min(num rows, num columns)" columns.

In conclusion these set of codes help exacute the Gaussian elemination effeciently by using methods like finding the maximum value in a column and then performing row or columns swap to help reduce the time taken to find the actual solution to our problem.
 

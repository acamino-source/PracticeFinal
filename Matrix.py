import numpy as np
import scipy.linalg as lalg
import numpy.matlib as npm

# creating a numpy 32x32 array A with normally distributed random numbers g_(i,j)~N(0,1) as it's elements
# this means a normal distribution with mu = 0 and standard deviation of 1.0
# if you want values only between 0 and 1 then use np.random.random((size, size))
A = np.random.normal(0,1,(32, 32))
print(A)

# calculating the inverse B= A^(-1)
B = lalg.inv(A)
print(B)

# transpose matrix
C = A.T
#print(C)

# find the determinant
determinant_A = lalg.det(A)
#print(determinant_A)

# The product of AB using the matrices A and B 
D = np.multiply(A, B)
print(D)

# The Dot product (dot and vector)
E = np.dot(A, B)
#print(E)

F = np.vdot(A, B)
#print(F)

# calculating eigenvalues and eigenvectors using scipy module .eig
eigenvalues, eigenvectors = lalg.eig(A)

print(eigenvalues)

print(eigenvectors)

op = "Charactristic equation of A is : (x-{})*(x-{})*(x-{})"
print(op.format(eigenvalues[0],eigenvalues[1],eigenvalues[2]))

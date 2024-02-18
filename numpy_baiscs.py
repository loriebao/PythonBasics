#define numpy array
import numpy as np

np1 = np.array([1, 2, 3])
np2 = np.array([4, 5, 6])

np3 = np.array([[11, 1, 2], [3, 4, 9], [18, 6, 5]])
np4 = np.array([[3, 6, 1], [6, 80, 4], [13, 8, 7]])

A = np.random.randint(1,100,(3,3))
b = np.random.randint(1, 10,(3))

print( f'add {np.add(np1, np2)}' ) 
print( f'subtract {np.subtract(np1, np2)}' ) 
print( f'multiply {np.multiply(np1, np2)}' ) 
print( f'dot {np.dot(np1, np2)}' ) 
print( f'inner {np.inner(np1, np2)}' ) 
print( f'outer {np.outer(np1, np2)}' ) 
print( f'det np3 {np.linalg.det(np3)}' ) 
print( f'det np4 {np.linalg.det(np4)}' ) 
print( f'inner np3.np4 {np.inner(np3, np4)}' ) 

print( f'det {A} {np.linalg.det(A)}' ) 
print( f'inv {A} {np.linalg.inv(A)}' ) 
print( f'solve {A}.x = {b} {np.linalg.solve(A, b)}' ) 

M1 = np.random.randint(1,100,(3,4))
M2 = np.random.randint(1, 10,(4,2))
print( f'{M1}.{M2} {np.dot(M1, M2)}' ) 

# print( f'add {np.add(np1, np2)}' ) 
# print( f'add {np.add(np1, np2)}' ) 
# print( f'add {np.add(np1, np2)}' ) 
  


   


#define numpy array
import numpy as np

np1 = np.array([1, 2, 3], dtype=np.int32)
np2 = np.array([4, 5, 6], dtype=np.int32)

np3 = np.array([[11, 1, 2], [3, 4, 9], [18, 6, 5]], dtype=np.int32)
np4 = np.array([[3, 6, 1], [6, 80, 4], [13, 8, 7]], dtype=np.int32)

A = np.random.randint(1,100,(3,3), dtype=np.int32)
b = np.random.randint(1, 10,(3), dtype=np.int8)

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

M1 = np.random.randint(1,100,(3,4), dtype=np.int32)
M2 = np.random.randint(1, 10,(4,2), dtype=np.int8)
M3 = np.dot(M1, M2)
print( f'{M1}.{M2} {np.dot(M1, M2)} {M1.dtype} {M2.dtype} {M3.dtype}' ) 

one_matrix = np.ones((6,4))
print( f'{one_matrix} {np.ndim(one_matrix)} {np.shape(one_matrix)}' )   
   
c = np.reshape(one_matrix, (2, 3, 4)) # 3d array
print(c)


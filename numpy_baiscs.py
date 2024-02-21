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
print(c.dtype, c.shape, c.size)

# -1 means auto cal the other dimension
x = np.linspace(0, 2 * np.pi, 10).reshape(2,-1)        # useful to evaluate function at lots of points
print(x.dtype, x.shape, x.size)
print(x)
f = np.sin(x)
print(f)

def myfunc(x, y):
    return np.sin(x+y)

b = np.fromfunction(myfunc, (5,2), dtype=np.float64)
print(b)
print(b[:,0]) #each row in first column
print(b[-1])   # the last row. Equivalent to b[-1, :]
# The reshape function returns its argument with a modified shape, 
# whereas the ndarray.resize method modifies the array itself
c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
               
print(c)
print(f'c.shape {c.shape}')

print(c.T)
print(f'c.shape {c.shape}')

c.resize((2, 6 ))
print(c)

print(c[1, ...])    # same as c[1, :, :] or c[1]
print(c[..., 2])    # same as c[:, :, 2]

print(f'c.flat {c.flat[:]}')
for i in c.flat:
    print(i, end = ' ')

rg = np.random.default_rng(1)  # create instance of default random number generator
a = np.floor(10 * rg.random((3, 4)))
print(a)    

#np.vstack((a, b))
#np.hstack((a, b))   

#Slicing an array returns a view of it:
s = c[:, 1:3]
s[:] = 10
print(c)

d = a.copy()  # a new array object with new data is created
print(d is a)
a = np.arange(int(1e8))
b = a[:10].copy()
del a  # the memory of ``a`` can be released.
print(b)

x = np.array([[1, 2], [3, 4]])
m = np.asmatrix(x)
print(x)
print(m)

#sorting:
ss = np.array([[0, 3], [2, 2]])
ind = np.argsort(s, axis=0)
print(ss)   
print(ind)  
print(np.sort(ss, axis=0))



import math
import  random
import numpy as np
from  scipy.optimize import minimize_scalar
from  scipy.optimize import fsolve

#############################LIST EXAMPLES: USE LIST AS A STACK#############################################
#list examples: initialize, append, pop, insert, extend, count, reverse, sort (in-place)
#use list as a stack is easy: last in, first out; append() ==> last in , pop() ==> first out
#initialize a list with 10 elements of string type

# """ 

"""
sorted_list = sorted(orig_list)
print(sorted_list)

orig_list.extend(sorted_list)
print(orig_list)

orig_list.sort()
print(orig_list)

orig_list.pop()
print(orig_list)
print(orig_list.count(8))   #returns the number of times 10 is present in the list

new_set = set(orig_list) 
print(new_set)
"""

# #comment out rest of the code below to see the output
# ##########################LIST EXAMPLES: USE LIST AS A QUEUE#####################################
# #use list as a queue: fist in, first out; To implement a queue, use collections.deque
"""
from collections import deque

# from operator import truediv
# from pickle import TRUE
# from tkinter import Y
# from xmlrpc.server import DocCGIXMLRPCRequestHandler
orig_list = []

for i in range(10): 
    orig_list.append(i) 
print(orig_list)

orig_list.pop()
print(orig_list)
orig_list.append(9)
print(orig_list)    

my_Q = deque(orig_list)
print(my_Q) 

my_Q.append(10)
my_Q.append(11)
print(my_Q)

e0 = my_Q.popleft()
e1 = my_Q.popleft()
e11 = my_Q.pop()
print(my_Q)

my_Q.appendleft(e1)
my_Q.appendleft(e0)
my_Q.append(e11)     
my_Q.remove(e1) 
print(my_Q) 
"""

# ##########################LIST EXAMPLES: LIST COMPREHENSION#####################################
"""
squares = [x**2 for x in range(1, 11)]
print(squares)  

list1 = [1, 4, 6,8, 9]
list2 = [3, 4, 6, 9, 2, 7]
tuple_list = [(x, y) for x in list1 for y in list2 if x!=y]
print(tuple_list)   
tuple_list.sort()
print(tuple_list)

#   #####nested list comprehesion#############
my_matrix = [
    [1,2,3,4],
    [2,3,4,5],
    [4,5,6,7],
]
print(my_matrix)

# #tranpose row and columes
# trans_matrix = list(zip(*my_matrix))
# print(trans_matrix)

tran_matrix = [[row[col] for row in my_matrix] for col in range(len(my_matrix[0]))]
print(tran_matrix)

del tran_matrix[1:4]
print(tran_matrix) 


# trans_matrix = []
# for i in range(len(my_matrix[0])):
#     trans_matrix.append([row[i] for row in my_matrix])
# print(trans_matrix)

# #USE zip(): it is an tranpose funtion, need to be wrapped in a list or iterate overthrough for loops to be useful
# #use zip(*iterables, strict=False): strict=True means row and col has to be the same
# trans_matrix = list(zip(my_matrix))
# print(trans_matrix)

# #zip() in conjunction with the * operator can be used to unzip a list:
# trans_matrix = list(zip(*my_matrix))
# print(trans_matrix)

# There is a way to remove an item from a list given its index instead of its value: the del statement. 
# This differs from the pop() method which returns a value.
# del trans_matrix[1:2]
# print(trans_matrix)
""" 

# ###############Tuples and Sequences and Set ###############################
"""
tp = (111, 2222, 'hello') #immutable 
x, y, z = tp #sequence unpacking
print(tp)
print(tp[1])
print(x, y ,z)

###########A set is an unordered collection with no duplicate elements.###################
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

#######Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a, b)                                  # unique letters in a
print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
c = a.union(b)                              # letters in a and b
print(c)    

print(a ^ b)                              # letters in a or b but not both
###print(a + b)                         # not supported in Python 3.6
"""

"""
# #############################DICTIONARY (key:value pair) EXAMPLES: #############################################
# mydict = {"kayla":15, "ally":11, "helen":11, "anna":12}
# print(mydict)
# print(mydict["kayla"])
# print(mydict.items())

# #########################HOW TO SWAP VALUES IN LIST/ARRAY###########################
# list1 = [1, 2, 3]
# tempval = list1[2]
# list1[2] = list1[0]
# list1[0] = tempval

# print (list1)

# # #########################FUNCTION DEFINTION###########################
# def my_function():
#     x, y = input("enter x = "), input("enter y = ")
#     return int(x) + int(y)
# 23

# while True:
#     a = my_function()
#     if a==0:
#         break;
#     else:
#         print(a)

# def my_concat(*word_list, sep='***'):
#     concatword =    sep.join(word_list)   
#     return concatword
# myword = my_concat("cat","eat","dog","food")
# print(myword)


# print(findword(myword))

# print(user_prompt.__doc__)
# # user_prompt("Are you a girl?")
# # user_prompt("Are you a boy?", 2, "Come on, try harder!")
# # user_prompt("Are you a boy?", retries=1, reminder="Dumb!")
"""

################## Modules: The file name is the module name. #########################
################## Within a module, the module’s name (as a string) is available as the value of the global variable __name__##########
"""
import fibo
import timeit

print(fibo.__name__)
myfibo2 = []
#print(timeit.timeit(lambda: fibo.fib(50), number=1))
print(timeit.timeit(lambda: fibo.fib2(50, myfibo2), number=100))
print(myfibo2)
"""

#enumerate through a tuple
# mytup = (random.randint(100, 180) for i in range(20))
# for i, a in enumerate(mytup):
#     print(i, a) 

# def f(x):
#     return (x+10)**2 - 20
#     # return x**3/(x**3 + (1-x)**3)

# mymin = minimize_scalar(f)

# print(mymin)
# import numpy as np
# from scipy.optimize import fsolve
# def func(x):
#     return [x[0] * np.cos(x[1]) - 4,
#             x[1] * x[0] - x[1] - 5]
# root = fsolve(func, [1, 1])

# print(root)

def pred(y):
    #x = 1/(1 + (1/((y/(1-y))^1/3)))
    
    n1 = y/(1-y)
    n2 = n1**(1/3)
    n3 = 1/n2
    n4 = n3+1
    n5 = 1/n4
    return n5
print(pred(0.6))

def pred(x):
    #y = (x/(1-x))^3/(1 + (x/(1-x))^3)
    
    n1 = (x/(1-x))**3
    n2 = n1/(1+n1)
    return n2
print(pred(0.5337374181795534))



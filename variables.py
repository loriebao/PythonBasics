from math import *

#abs, pow, min, max, round, floor, ceil, sqrt
a = -23
b = abs(a)
print(b)

c = min(a, b)
print(c)

a = "cool stuff"
b = 1234.5
c = True

print("a = ", a)
print("b = ", b)
print("c = ", c)
print(b, "is", a)

student_name = "Anna"
student_age = 12
print("Ms. Lorie has a student named", student_name, "and her age is", student_age)

print(student_name.upper())
print(student_name.isupper())
print(len(student_name))
print(student_name[0])
print(student_name.index('n'))
#print(student_name.index('Z'))
print(student_name.replace('nna', 'lly'))
print(a.replace('cool', 'odd'))

a = 5
b = str(a)
c = a + "is my favorite number"
d = b + "is my favorite number"

#from math import *
#abs, pow, min, max, round, floor, ceil, sqrt

#get input from user
name = input("enter your name: ")
age = input("enter your age: ")
print("Hello " + name + "!" + "You are " + age)
int_age = int(age)
float_age = float(age)

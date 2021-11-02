# Week 1
# Example Solutions to Exercises

#---------------------------------------------------------------

# 1.1 Introduction
import keyword
print(keyword.kwlist)

#---------------------------------------------------------------

# 1.2 - Variables
# Exercise 1 - Numbers and Arithmetic Operators

# 1
A = 6
B = 5

# 2
print(A + B)

# 3 
E = A * B

# 4
E = (A+B)/3

# 5
print(A % B)

# 6
pi = 3.142
r = 1
v_sphere = (4/3) * pi * r**3  # volume of a sphere
print(v_sphere)

# 7
l, w, h = 1, 4, 5
v_cuboid = l * w * h

#---------------------------------------------------------------

# Exercise 2 - Strings

# 1
C = 'Hello'
D = 'world'

# 2
new_string = (C + ' ' + D)
print(new_string)

# 3
print(C[2])

#4
print(D[2:5])
print(D[2:])
print(D[-3:])

#---------------------------------------------------------------

ADVANCED QUESTIONS

# A
# square root of r
print(r ** (1/2)) 

# round a number to nearest integer
P = 10.7
rounded = (P + 0.5) // 1
print('P rounded=', rounded)

# shift an integer in range of integers by a certain value
orig = 2
shift = -4
hi = 10
lo = 1

# number of values in range
N = hi-lo+1 

# shifted value
K = (lo-1) + ((orig + shift - hi) % N)

# B 

val = False
var = True 

print(val + var)
print(val * var)
print(val % var)

#---------------------------------------------------------------

# 1.3 Operators
# Exercise 3 - Comparison Operators


# 1 
print(A > B)

# 2
print(type(A) == type(B))

# 3
print(C[0] == D[0])

# 4
print('The volume of the sphere is greater: ', v_sphere > v_cuboid)
cuboid_greater = v_cuboid > v_sphere
print('The volume of the cuboid is greater: ', cuboid_greater)

# #---------------------------------------------------------------

# Exercise 4 - Logical Operators

# 1
print (not(A % 2) and not(B % 2))

# 2
print (not(A % 2) or not(B % 2))

# 3
Valentina = 70
Hendrik = 65
Anthony = 30

print(Valentina > 40 or Hendrik > 40 or Anthony > 40)

# ADVANCED QUESTIONS

# A
eats_plants = True
eats_meat = False

herbivore = eats_plants and not(eats_meat)
carnivore = eats_meat and not(eats_plants)
omnivore = eats_plants and eats_meat

# B
n = 23
square = (n ** (1/2)) / int (n ** (1/2)) == 1
print(square)

















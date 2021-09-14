#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:36:54 2021

@author: hemma
"""
# Week 2 

# Exercise 1 - Variable types
# Cast an integer variable with value 8 as:
# - item a floating point number.
# - item a boolean value.
val = 8
val_f = float(val)
val_b = bool(val)
    
# Exercise 2 - Strings
# Assign a few words or a short sentence a variable, my_reason_for_learning_python
# Then print it
my_reason_for_learning_python = "Programming is fun and useful"
print(my_reason_for_learning_python)

# Exercise 3 - Lists
# Use a built-in python function to print the length of the list [2, 3, 4, 5]
# Edit the list to add the number 6 to the end of the list
# Edit the list to add the number 1 to the beginning of the list
my_list = [2, 3, 4, 5]
print(len(my_list))
my_list.append(6)
my_list.insert(0, 1)
print(my_list)

# Exercise 4 - Control flow 
# Write a program that prints the numbers from 1 to 50, inclusive, and: 
# skips multiples of three 
# prints “Multiple of 5” instead of multiples of five 
# prints “!” instead of multiples of both three and five.
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("!")
    elif num % 3 == 0:
        continue
    elif num % 5 == 0:
        print("Multiple of 5")
    else:
        print(num)



# Week 3 

# Exercise 5 - Data structures
# 5.1. Print the largest number from a list, seperated by commas, input by the user.
nums = input("Input list of numbers, seperated by commas ")
nums = [float(x) for x in nums if x!=',' and x!=' ']
print(max(nums))


# 
# 5.2. Create a dictionary with key (x) value (x^2) pairs for x = integers 1 to 5

d = {1: 1**2,
     2: 2**2,
     3: 3**2,
     4: 4**2,
     5: 5**2
     }

print(d)


# OR

d = dict()
for x in range(1,6):
    d[x]=x*x

print(d) 

# 5.3 Print the 4th element of the tuple ("red", "green", "blue", "pink", "gold")
# using its index. 
t = ("red", "green", "blue", "pink", "gold")
print(t[3])

# Exercise 6 - Loops
# 6.1 Use a for loop to print each student and grade stored as the following 
# two loops:
# students = ["Jay", "Kip", "Laura"]
# grades = [66, 52, 76]
# in the format student : grade (e.g. Jay : 66)
students = ["Jay", "Kip", "Laura"]
grades = [66, 52, 76]
for s, g in zip(students, grades):
    print(f"{s} : {g}")


# 6.2 Use a for loop to reverse a string
word = "desserts"
rev_word = ''
for w in word[::-1]:
    rev_word += w
print(rev_word)
    

# Week 4 

# Exercise 7 - Function
# 7.1 Write a function calculation() that accepts two variables, calculates: 
# a) the sum of two variables 
# b) division of first variable by second variable 
# and then returns both a) and b) in a single return call. 
# Call your function and assign a) and b) to two seperate global variables
def calculation(a, b):
    return a+b, a/b
sum_, div_ = calculation(8, 2)
print(sum_, div_)

# 7.2 Create a function showStudent() in such a way that it should accept student 
# name, and their mark out of 100 and display both, but of the mark is missing 
# in the function call it should show it as "absent"
def showStudent(name, mark='absent'):
    print(f" Name: {name} \n Mark: {mark}")
Alice = showStudent("Alice", 66)
Majid = showStudent("Majid")


# Week 5 

# Exercise 8 - Classes
# Create a Student class and initialize it with name and student number. 
# Write methods:
# 1. display - display all information currently held about the student
# 2. setAge - assign an age to student
# 3. setMarks - assign a mark out of 100 to the student

# NOTE: This is  working solution using the techniques we have learnt so far 
# on this course. In Further Computer Programming you can learn more efficient 
# methods for solving problems like these. 
    
class Student():
    def __init__(self, name, s_num):
        self.name = name
        self.s_num = s_num
        self.age = 'None'
        self.mark = 'None'
        
    def display(self):
        print(self.name, self.s_num, end=' ')        
        if self.age != 'None' and self.mark != 'None':
            print(self.age, self.mark)
        elif self.age != 'None':
            print(self.age)
        elif self.mark != 'None':
            print(self.mark)
        else:
            print()
            
    def setAge(self, age):
        self.age = age
        
    def setMArk(self, mark):
        self.mark = mark
        
s = Student('h', 24)

s.display()
s.setAge(18)
s.display()        
    

# Week 6 

# Exercise 9 - Writing files
# Write your answer to Exercise 8 to a .txt file. 
with open('students.txt', 'a') as file:
    for s, g in zip(students, grades):
        file.write(f"{s} : {g}\n")
        

# Exercise 10 - Command line, importing python files
# Store the function you wrote for Exercise 11 in a file funcs.py
# Call the function in another program main.py
# Run main.py from the command line


# Week 7 
# Exercise 11 - Numpy
# Create the numpy array
# [[24, 22, 20, 18],
#  [16, 14, 12, 10],
#  [8,  6,  4,  2]] 

# Multiply:
# 1st column by 2
# 2nd column by 3
# 3rd column by 4
# 4th column by 5
import numpy as np
m = np.arange(24, 1, -2)
m = m.reshape(3, 4)
print(m) 

print(m * [2, 3, 4, 5])


# Week 8   
# Excercise 12 - Matplotlib 
# Plot a bar chart of the students and their grades in Exercise 8

import matplotlib.pyplot as plt

x = np.arange(len(students))
y = grades
plt.bar(x, y)
plt.xticks(x, students)
plt.xlabel('students')
plt.ylabel('grades')
plt.show()

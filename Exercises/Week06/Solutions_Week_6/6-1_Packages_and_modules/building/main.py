#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:49:10 2021

@author: hemma
"""
# if * is used, math and funcs both contain a function ceil
# if funcs is imported first, the program will crash

from math import *   
from house import *
from funcs import *

area = ceil(width, length)

print(f'The area of the ceiling on floor {floor} is {area} m2')

theta = pi/6

roof_height = width/2 * tan(theta)

print(roof_height)



# If namespaces are used, this issue is avoided
from house import *
from funcs import *
import math  

area = ceil(width, length)

print(f'The area of the ceiling on floor {floor} is {area} m2')

theta = math.pi/6

roof_height = width/2 * math.tan(theta)

print(roof_height)



# A function to calculate height can be imported from a different file
# math should be imported to the file where functions and variables are defined rather than called 
from house import *
from funcs import *
#import math  

area = ceil(width, length)

print(f'The area of the ceiling on floor {floor} is {area} m2')


roof_height = height(theta, width)

print(roof_height)
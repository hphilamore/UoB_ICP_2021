""" 
There are a number of ways to deal with the need for constants e.g. pi
The most reliable way to ensure a constant value is used is to import it from:
    - an external package e.g. math (for well known constants like pi)
    - a user-defined library for program-specific constants
"""
# Exercise 2.3    

#from spheres.sphere import *  # if pi defined by deveoper in sphere.py
from spheres import *
sphere = Sphere(5)

# OR

# import spheres.sphere as s    # if pi imported in sphere.py
# sphere = s.Sphere(5)


print(sphere.volume(), 'm3')

# Exercise 2.6 
from spheres.dimensions import *
sphere_2 = Sphere(radius)


# Exercise 3.3
import sys
sys.path.append('../')
import cube

# Exercise 5.3
import new_file

C = cube.Cube(radius)
print(C.area())

new_file.my_func()






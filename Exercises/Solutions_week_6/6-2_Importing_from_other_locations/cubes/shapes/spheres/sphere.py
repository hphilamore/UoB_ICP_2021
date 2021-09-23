# Exercise 2.1, 2.2
from math import pi as pi # pi imported

# pi = 3.142              # pi defined

class Sphere():
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return pi * self.r**2
        
    def volume(self):
        return (4/3) * pi * self.r**3
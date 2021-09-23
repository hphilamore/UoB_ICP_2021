# Exercise 3.1, 3.2

class Cube():
    def __init__(self, L=1):
        self.L = L
    def volume(self):
        return self.L**3
    def area(self):
        return self.L**2 * 6
    
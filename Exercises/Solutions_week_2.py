# Week 1
# Example Solutions to Exercises

#---------------------------------------------------------------

# 2.1 Conditionals
# Exercise 1 - if elif else

# 1
A = 2
B = 3
num = A - B

if num < 0:
    print('negative')
elif num > 0:
    print('positive')
else:
    print('zero')
    
# 2
Valentina = 30
Hendrik = 30
Anthony = 30

if (Valentina > 40 and Hendrik > 40 and Anthony > 40):
    print('All student passed')
    
elif (Valentina > 40 or Hendrik > 40 or Anthony > 40):
    print('Some students passed')
    
else:
    print('No students passed')
    
# 3
C = 'Elephant'

if (C[0] == 'A' or
    C[0] == 'a' or
    C[0] == 'E' or
    C[0] == 'e' or
    C[0] == 'I' or
    C[0] == 'i' or
    C[0] == 'O' or
    C[0] == 'o' or
    C[0] == 'U' or
    C[0] == 'u'):
    print(C, 'starts with a vowel')
    
# 4
GBP = 25
R = 1.38
if GBP < 50:
    M = 0.9
elif 50 <= GBP < 500:
    M = 0.92
elif 500 <= GBP < 5_000:
    M = 0.95
elif 5_000 <= GBP < 50_000:
    M = 0.97
else:
    M = 0.98
 
USD = GBP * M * R

print('USD=', USD, ', effective exchange rate=', USD/GBP)
#---------------------------------------------------------------

# ADVANCED QUESTIONS

# A
# coordinates of a point
P_x = -3
P_y = 0

# coordinates of circle centres
C1_x = 0
C1_y = 0

C2_x = 2
C2_y = 1

C3_x = -5
C3_y = 0

# radius of each circle
C1_r = 5
C2_r = 2
C3_r = 3

# Euclidean distance from the point to each of the circle centres
P_to_C1 = ((P_x - C1_x)**2 + (P_y - C1_y)**2)**(1/2)
P_to_C2 = ((P_x - C2_x)**2 + (P_y - C2_y)**2)**(1/2)
P_to_C3 = ((P_x - C3_x)**2 + (P_y - C3_y)**2)**(1/2)

print(P_to_C3)

# Test if point lies in each circle:
# Check if the distance from the point to the centre of the circle is less than or equal to the radius of the circle. 
if P_to_C2 <= C2_r:
    print("The point ", P_x, ',', P_y, " is in circle C2.")
    print("The point ", P_x, ',', P_y, " is in circle C1.")
elif P_to_C1 <= C1_r:
    print("The point ", P_x, ',', P_y, " is in circle C1.")
        
if P_to_C3 <= C3_r:
    print("The point ", P_x, ',', P_y, " is in circle C3.")   
    
#---------------------------------------------------------------

# 2.2 User input and nested conditionals
# Exercise 2 - User Input

# 1 
num = int(input('Enter a number: '))

if num < 0:
    print('negative')
elif num > 0:
    print('positive')
else:
    print('zero')
    
    
# 2
name = input('Enter your name: ')
print('Your name ends with the letter ', name[-1])

# Exercise 3 - Nested conditionals

# 1
name = input('Enter student name: ')
score = int(input('Enter student score: '))

if score >= 40:
    if 40 <= score < 50:
        G = 'D'
    elif 50 <= score < 60:
        G = 'C'
    elif 60 <= score < 70:
        G = 'B'
    else:
        G = 'A'
        
    print(name, ' passed with grade ', G)
    
else:
    print(name, ' failed')
    

# 2
key =  input(
'''You approach a castle.
The castle door is closed.
You find a key.
Do you pick up the key? (Y/N): ''')

if key == 'Y':
    print('Magic key turns you into a frog. \n You lose!')
    
elif key == 'N':
    print('Castle door opens.')
    castle = input('Do you enter the castle? (Y/N)')
    
    if castle == 'Y':
        print('Find treasure.\nYou win!')
    elif castle == 'N':
        print('No treasure.\nYou lose!')
else:
    print('Invalid input. Exiting game.')
        
    
      
    
    
        
    




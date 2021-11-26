# # Week 9
# # Example Solutions to Exercises

# #---------------------------------------------------------------

# # 9.1 Reading and Writing Files

# # Exercise 1 - Plotting

import matplotlib.pyplot as plt

# # 1,2
# x = [0,2,4,5,8,10,13]
# y = [1,3,3,3,4,5,6]
# plt.plot(x, y, 'xm--') 
# plt.show()


# # 3
# f = [-3,0,1,0,4,6,7]
# plt.plot(x, y, 'xm--')
# plt.plot(x, f, '.g-')
# plt.show()


# # 4
# plt.plot(x, y, 'xm--', label = "y")
# plt.plot(x, f, '.g-', label = "f")
# plt.xlabel("x")
# plt.title("Plot of y,f vs x")
# plt.legend()
# plt.show()


# # 5
# plt.plot(x, y, 'xm--', label = "y")
# plt.plot(x, f, '.g-', label = "f")
# plt.xlabel("x")
# plt.title("Plot of y,f vs x")
# plt.legend()
# plt.savefig('my_plot.pdf')
# plt.show()


# 6
import numpy as np
def power(x,n):
    return(x**n)

x = np.arange(0,11,1)

for n in range(2,5):
    plt.plot(x, power(x, n), label=f'x^{n}')
    
plt.xlabel('x')

plt.legend()
    
plt.show()


# 7
plt.subplot(311)
plt.plot(x, power(x,2))
plt.ylabel('x^2')

plt.subplot(312)
plt.plot(x, power(x,3))
plt.ylabel('x^3')

plt.subplot(313)
plt.plot(x, power(x,4))
plt.ylabel('x^4')

plt.xlabel('x')

plt.show()


# #---------------------------------------------------------------

# # Exercise 2 - Histograms and importing data

# # 1
import csv

# # def diceRolls(n):
# #     with open('diceRolls.csv',mode='w') as file:
# #         return np.random.randint(1,7,n)
    
# # diceRolls(n)
        

# # 2
# def diceRolls(n):
#     with open('diceRolls.csv',mode='w', newline='') as file:
#         write = csv.writer(file, delimiter = ',')# setting the delimiter to comma in accordance with the csv format
#         write.writerow(np.random.randint(1,7,n))
        
        
# # 3
# # Method using numpy to import 
# diceRolls(100)
# data = np.loadtxt('diceRolls.csv', delimiter=',')
# print(data)

# # OR

# # Method using csv module to import
# with open('diceRolls.csv') as csvfile:
#     file = csv.reader(csvfile)
#     for row in file:
#         data = row
#     data = [int(d) for d in data]
#     data = np.array(data)
#     print(data)
       

# # 4
# plt.plot(data, '.')
# plt.show()


# # 5
# plt.hist(data, 
#           bins=np.arange(1, 8), 
#           edgecolor="k",
#           align ='left')


# # 6
# plt.title('distribution of dice rolls')
# plt.xlabel('value')
# plt.ylabel('frequency')

# # 7
# plt.savefig('hist.png') # Question 7
# plt.show()


# # 8
# students = np.loadtxt('sample_student_data.txt', 
#                       dtype=str, 
#                       skiprows=2) 

# print(students)

# # 1. Create a numpy array with the same number of positions as bars
# n_students = students.shape[0]
# x_pos = np.arange(n_students)

# # # 2. Generate bar chart
# plt.bar(x_pos, students[:,4].astype(float))

# # # 3. Replace x ticks with bar names
# # # (Rotate labels 30 degrees)
# print(students[:,0])
# plt.xticks(x_pos, students[:,0], rotation=90)

plt.show()


# # 9
students = np.loadtxt('sample_student_data.txt', 
                      dtype=str, 
                      skiprows=2)

height = students[:, 3]           # select hieght data
 
height = height.astype(float)   # convert to float

# histogram
plt.hist(height, bins=10);           # equally spaced bins between minimum and maximum values can be auto-generated 

# add label
plt.xlabel('height')
plt.ylabel('frequency')

plt.show()








# #---------------------------------------------------------------

# # ADVANCED QUESTIONS

# # A
# import numpy as np
# np.set_printoptions(suppress=True)
# A = np.loadtxt('douglas_data.csv', 
#                 delimiter=',',
#                 skiprows=2, 
#                 usecols=(list(range(1,9)))
#                 )

       
# # B
# data = A[:10,:] # first 10 values
# print(data)

# data[:, -1] = data[:, -1] * 10**6 # convert N/mm2 to N/m2
# print(data)       

# # C
# np.set_printoptions(suppress=True)

# print(data.shape)                       # view number of rows, columns
                    
# mass = 0.01 * data[:,4] * data[:,5]/100 # calculate mass

# data = np.c_[ data, mass]               # add a column

# print(data.shape)                       # check a column has been added


# # D
# plt.subplot(211)    # 2 rows, 1 column, index 1
# plt.plot(data[:,1], data[:,7], '.r')



# plt.subplot(212)    # 2 rows, 1 column, index 2
# # 1. Create a numpy array with the same number of positions as bars
# x_pos = np.arange(data.shape[0])

# # 2. Generate bar chart
# plt.bar(x_pos, data[:,-1]);

# # 3. Replace x ticks with field name
# samples = np.loadtxt('douglas_data.csv', # import sample names 
#                 delimiter=',',
#                 skiprows=2, 
#                 usecols=0,
#                 dtype=str
#                 )
# samples = samples[:10] # slect first 10
# plt.xticks(x_pos, samples, rotation=30);

# # 4. Add axis labels 
# plt.xlabel('sample');
# plt.ylabel('mass');

# plt.show()


# E

# students = np.loadtxt('sample_student_data.txt', 
#                       dtype=str,        # mixed data types can be imported as string data
#                       skiprows=2)       # exclude header


# female = students[students[:,1]=='F']   # all rows, where column 1 == F
# print(female)

# height = female[:, 3]                   # select hieght data
 
# height = height.astype(float)           # convert to float

# # histogram
# plt.hist(height, bins=10);              # equally spaced bins between minimum and maximum values  

# # add label
# plt.xlabel('height')
# plt.ylabel('frequency')


# #---------------------------------------------------------------

# # 9.2 Curve fitiing

# import numpy as np
# import matplotlib.pyplot as plt

# # Exercise 3 - Polynomials
# # 1
x = [1, 6, 3, 4, 10, 2, 7, 8, 9, 5]
y = [2, 4, 5, 4, 13, 3, 4, 8, 12, 4]
# Find coefficients of polynomial
coeffs_3 = np.polyfit(x, y, 3)

# Generate fitted data 
yfit3 = np.polyval(coeffs_3,x)

# RMSE 

def RMSE(x, y, yfit):
     "Returns the RMSE of a polynomial of specified order fitted to x-y data"
     # error
     e = (yfit - y)  
     # RMSE
     return np.sqrt(np.sum(e**2)/ len(x))


rmse = RMSE(x,y,yfit3) # using RMSE function defined in earlier example 


# # 2
# x = np.sort(np.random.uniform(1.0,10.0,20))
# y = np.sort(np.random.uniform(1.0,10.0,20))

# print(x, y)

# # 3 
# plt.scatter(x,y)
# plt.show()

# # 4 & 6
# coefs_2  = np.polyfit(x,y,2)  
# coefs_5  = np.polyfit(x,y,5) 

# # 4 & 6
# yfit_2 = np.polyval(coefs_2,x)
# yfit_5 = np.polyval(coefs_5,x)
# plt.plot(x, y, 'ko')
# plt.plot(x, yfit_2, label='poly deg. 2')
# plt.plot(x, yfit_5, label='poly deg. 5')
# plt.legend()
# plt.show()

# # 7
 

# print('RMSE poly degree 2: ', RMSE(x, y, yfit_2))
# print('RMSE poly degree 5: ', RMSE(x, y, yfit_5))

# Exercise 4 - Fitting Arbitrary Functions
from scipy.optimize import curve_fit
# 1
s = np.loadtxt('signal_data.csv', dtype=float, delimiter=',')
x = s[0]
y = s[1]

# 2
# DEFINE FUNCTION TO FIT 
def sin_func(x, a, b):             
    y = a * np.sin(x + b) 
    return y

# FIT CONSTANTS
c, cov = curve_fit(sin_func, x, y)  
c = curve_fit(sin_func, x, y)[0]


# 3
# GENERATE FITTED DATA
x_new = np.array(sorted(x))         # sort x data monotonically
y_fit = sin_func(x_new, *c)         # run function on sorted data


# PLOT
plt.plot(x,     y,     'o',    label='raw')
plt.plot(x_new, y_fit, 'r',    label='fit')
plt.legend(loc='best');    
plt.show()            


# #---------------------------------------------------------------

# # ADVANCED QUESTIONS

# # A
# import numpy as np
# from scipy.optimize import curve_fit


# np.set_printoptions(suppress=True)
# A = np.loadtxt('douglas_data.csv', 
#                 delimiter=',',
#                 skiprows=2, 
#                 usecols=(list(range(1,9)))
#                 )

      
# # B
# # scatter plot of raw data
# x = A[:, 1]
# y = A[:, 7]
# plt.plot(x, y, 'o')  
# plt.show() 

# # C
# # write a Python function for a function you can see in the data
# def func(x, a, b, c):
#     return a * np.exp(-b*x + c)

# # fit constants of the function
# c = curve_fit(func, x, y)[0]

# # D 
# # generate fitted data
# x_new = np.array(sorted(x))
# y_fit = func(x_new, *c)

# # E, F
# # plot fitted and raw data
# plt.plot(x, y, 'o')
# plt.xlabel('knot ratio')
# plt.xlabel('bend strength (N/mm2)')
# plt.plot(x_new, y_fit, label=f'{np.round(c[0], 2)}e^(-{np.round(c[1],2)}x+{np.round(c[2],2)})')
# plt.legend()
# plt.show()

# # G
# print('RMSE = ', RMSE(x, y, y_fit))


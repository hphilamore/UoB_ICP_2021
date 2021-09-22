# Week 7
# Example Solutions to Exercises

#---------------------------------------------------------------

# 7.1 Reading and Writing Files

# Exercise 1 - Writing files

# 1 
header = ['sample', 'mass(kg)']
sample = ['A', 'B', 'C', 'D', 'E']
mass = [0.600, 0.455, 0.550, 0.505, 0.550]

file = open('../sample_data/samples.txt', 'w')

file.write(header[0] + ' ' + header[1] + '\n')

for s, m in zip(sample, mass):
    file.write(s + ' ' + str(m) + '\n')
    
file.close()

# OR

table = {'sample' : 'mass(kg)',
          'A' : 0.600,
          'B' : 0.455,
          'C' : 0.550,
          'D' : 0.505,
          'E' : 0.550}

file = open('samples.txt', 'w')
for k, v in table.items():
        file.write(k + ' ' + str(v) + '\n')
file.close()
        
# 2
file = open('../sample_data/samples.txt', 'a')
file.write('F 0.505 \n')
file.write('G 0.535 \n' )
file.close()

#----------------------------------------------------------------------------        
        
# Exercise 2 - Reading files

# 1 
f = open('../sample_data/samples.txt', 'r')
print(f.read())
file.close()

# 2
f = open('../sample_data/samples.txt')
print(list(f)[3])
file.close()

# OR

f = open('../sample_data/samples.txt')
print(f.readlines()[3])
file.close()


# 3
mass = []
f = open('../sample_data/samples.txt') 
for line in f.readlines()[1:]:              # make file object a list of lists so loop can begin on 2nd entry
    L = line.split()                  # split the line ito words
    mass.append(float(L[1]) * 1_000)  # convert to numerical data, convert to grams, and add to list containing column data
print(mass)
f.close()

# OR

mass = []
f = open('../sample_data/samples.txt', 'r')
for line in f:
    L = line.split()                           # split the line ito words
    mass.append(L[1])                          # add to list of column data
    
masses = [float(m) * 1_000 for m in mass[1:]]  # convert values excludig heading to numerical data, convert to grams  
print(masses)

#----------------------------------------------------------------------------
    
# Exercise 3-Reading and writing files

# 1
with open('../sample_data/samples.txt', 'r+') as file:
    lines = file.readlines()   # lines as list of strings
    upper = lines[0].upper()   # convert first line to upper case
    print(upper)
    file.seek(0)               # go to start of file
    file.write(upper)          # overwrite existing line
    # file.seek(0)               # go to start of file
    # print(file.read())         # print file contents (not returning to start will print contents starting after header)
    

# 2 
# with open('../sample_data/price_per_item.csv', 'r+') as file:
#     print(file.read()) 
#     file.write('24, chips, 2.00 \n')
#     file.seek(0)
#     print(file.read())
    

#----------------------------------------------------------------------------

# ADVANCED EXERCISES

# A
samples = []
mass = []
with open('../sample_data/samples.txt', 'r+') as f:
    for line in f.readlines():        # read data
        L = line.split()         
        samples.append(L[0])          # collect column data as lists
        mass.append(L[1])
    
    mass[2] = 0.485                   # overwrite old mass list
    table = list(zip(samples, mass))  # transpose the column data to row data
    f.truncate(0)                     # erase the file contents 
    for line in table:
        f.write(line[0] + ' ' + str(line[1]) + '\n' ) # write edited table to file

        
# B
samples = []
mass = []
with open('../sample_data/samples.txt', 'r+') as f:
    for line in f.readlines():                        # read data
        L = line.split()         
        samples.append(L[0])                          # collect column data as lists
        mass.append(L[1])
    mass_r = [round(float(m), 2) for m in mass[1:]]   # convert all numerical data in mass column to float and round to 2 d.p.
    mass = [mass[0]] + mass_r                         # overwrite old mass list
    table = list(zip(samples, mass))                  # transpose the column data to row data
    f.truncate(0)                                     # erase the file contents 
    for line in table:
        f.write(line[0] + ' ' + str(line[1]) + '\n' ) # write edited table to file
        
#----------------------------------------------------------------------------

#  7.2 Imported Modules for Reading and Writing Files 

#  Exercise 4 - Writing csv files 

# 1
      



        

        

        
        
    
        
    
 
    
 
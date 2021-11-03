# Week 7
# Example Solutions to Exercises

#---------------------------------------------------------------

# 7.1 Reading and Writing Files

# Exercise 1 - Writing files

# 1 
header = ['sample', 'mass(kg)']
sample = ['A', 'B', 'C', 'D', 'E']
mass = [0.600, 0.455, 0.550, 0.505, 0.550]

file = open('samples.txt', 'w')

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
file = open('samples.txt', 'a')
file.write('F 0.505 \n')
file.write('G 0.535 \n' )
file.close()

#----------------------------------------------------------------------------        
        
# Exercise 2 - Reading files

# 1 
f = open('samples.txt', 'r')
print(f.read())
file.close()

# 2
f = open('samples.txt')
print(list(f)[3])
file.close()

# OR

f = open('samples.txt')
print(f.readlines()[3])
file.close()


# 3
mass = []
f = open('samples.txt') 
for line in f.readlines()[1:]:              # make file object a list of lists so loop can begin on 2nd entry
    L = line.split()                        # split the line ito words
    mass.append(float(L[1]) * 1_000)        # convert to numerical data, convert to grams, and add to list containing column data
print(mass)
f.close()

# OR

mass = []
f = open('samples.txt', 'r')
for line in f:
    L = line.split()                           # split the line ito words
    mass.append(L[1])                          # add to list of column data
    
masses = [float(m) * 1_000 for m in mass[1:]]  # convert values excludig heading to numerical data, convert to grams  
print(masses)


# 4
print(min(masses))

  



#----------------------------------------------------------------------------
    
# Exercise 3-Reading and writing files

# 1
with open('samples.txt', 'r+') as file:
    lines = file.readlines()   # lines as list of strings
    upper = lines[0].upper()   # convert first line to upper case
    print(upper)
    file.seek(0)               # go to start of file
    file.write(upper)          # overwrite existing line
    # file.seek(0)             # go to start of file
    # print(file.read())       # print file contents (not returning to start will print contents starting after header)
    

# # 2 
# with open('price_per_item.csv', 'r+') as file:
#     print(file.read()) 
#     file.write('chips, 2.00 \n')
#     file.seek(0)
#     print(file.read())


# 3 
def new_item():
    with open('price_per_item.csv', 'r+') as file:
        print(file.read()) 
        new_item = input('Enter new food item: ')
        new_price = input('Enter new price: ')
        file.write(new_item + ',' + new_price + '\n')
        file.seek(0)
        print(file.read())

#new_item()

# # 4
# import item_adder
# item_adder.new_item()

# from item_adder import new_item
# new_item()
   

#----------------------------------------------------------------------------

# ADVANCED EXERCISES

# A
samples = []
mass = []
with open('samples.txt', 'r+') as f:
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
with open('samples.txt', 'r+') as f:
    for line in f.readlines():                        # read data
        L = line.split()         
        samples.append(L[0])                          # collect column data as lists
        mass.append(L[1])
    mass_r = [round(float(m), 2) for m in mass[1:]]   # convert all numerical data in mass column to float and round to 2 d.p.
    mass = [mass[0]] + mass_r                         # overwrite old mass list
    table = list(zip(samples, mass))                  # transpose the column data to row data
    f.truncate(0)                                     # erase the file contents
    f.seek(0)                                         # go to start of file
    for line in table:
        f.write(line[0] + ' ' + str(line[1]) + '\n' ) # write edited table to file
        
#----------------------------------------------------------------------------

#  7.2 Imported Modules for Reading and Writing Files 

#  Exercise 4 - Writing csv files 

# 1
import csv

header = ['sample', 'mass(kg)']
sample = ['A', 'B', 'C', 'D', 'E']
mass = [0.600, 0.455, 0.550, 0.505, 0.550]

# Method using loop
with open('samples.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for s,m in zip(sample, mass):
        writer.writerow([s, m])
    
# OR

# Method using zip to transpose data in rows to data in columns
data = [sample, mass]

data = list(zip(*data)) # or data = list(zip(sample, mass))

with open('samples.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)  # add hearder to each column
    writer.writerows(data)   # add data, transposed into columns


# 2
with open('samples.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['F', 0.505])
    writer.writerow(['G', 0.535])

# 3 
numbers = [1, 2, 3, 4, 5]
with open('numbers.txt', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerow(numbers)

    
    
#----------------------------------------------------------------------------

# Exercise 5 - Reading csv files 

# 1
with open('douglas_data.csv') as f:
    read = csv.reader(f)
    for r in read:
        print(r)
        
# 2 
with open('douglas_data.csv') as f:
    data = list(csv.reader(f))
    
    print(data)                           # display data to find density column number
        
    data = list(zip(*data[2:]))           # transpose data from header to rows (lists)
    
    density = data[5]                     # select density data 
    
    density = [float(d) for d in density] # convert to numerical data
    
    print(max(density))                   # print max
    
    
    
# 3
import csv
with open('samples.csv') as f:
    reader = list(csv.reader(f))               # read and convert to list
    
    ##########################################################
    
    #data = list(zip(*reader[1:]))             # trasnpose columns to list of lists, excluding header
    #mass = [float(d) for d in data[1]]        # convert 2nd column to float data
    
    # OR 
    
    mass = [float(d[1]) for d in reader[1:]] # assemble 2nd item of each row as list and convert to float data
    
    ##########################################################
    
    print(sorted(mass)) 
    
    
# 4
import csv

with open('price_per_item.csv') as file:
    reader = csv.reader(file)
    reader = list(reader)
    price = [float(r[1]) for r in reader[1:]]
    print(price)
    
    total = sum(price)
    mean = total / len(price)
    
    # SD using a for loop
    sum_squares = 0
    for i in price:
        sum_squares += (i - mean)**2
    ave_sum_squares = sum_squares / len(price)
    SD = ave_sum_squares ** (1/2)
    
    # SD using a list comprehension
    SD = ( sum([(i - mean)**2 for i in price]) / len(price) )** (1/2)
        
    print('mean=', mean)
    print('SD=', SD)

#----------------------------------------------------------------------------

Exercise 6 - Reading and writing csv files 
1
with open('price_per_item.csv', 'r+', newline='') as f:
    writer = csv.writer(f)
    reader = csv.reader(f)
    
    for line in reader:
        print(line)
        
    new_food = input('Enter new food: ')
    new_price = input('Enter price: ')
        
    writer.writerow([new_food, new_price])

    

#----------------------------------------------------------------------------

# ADVANCED EXERCISES - Reading and writing csv files
import csv


# A
volume = [336, 231, 350, 272, 300, 312, 255] # cm3


with open('samples.csv', 'r+', newline='') as f:
    reader = csv.reader(f)
    writer = csv.writer(f)
    
    data = list(reader)  # convert to list to manipulate columns
    
    for line in data:    # view data
        print(line)
    
    header = data[0]     # column headings
    
    ##########################################################
    
    # data_rows = list(zip(*data[1:]))      # transpose data in columns to rows
    # samples = data_rows[0]                # sample name  
    # mass = data_rows[1]                   # sample mass 
    # mass = [float(m) for m in mass]       # convert to numerical data
    
    # OR
    
    samples = [d[0] for d in data[1:]] 
    mass = [float(d[1]) for d in data[1:]]
    
    
    ##########################################################  
    
    
    density = [m / v*10**3 for m, v in zip(mass, volume)]  # calculate density
    
    header = header + ['volume(cm3)', 'density(kg/m3)']    # add new column names
    
    data = [samples, mass, volume, density]                # assemble data set

    f.truncate(0)                                          # erase file
    f.seek(0)                                              # go to start of file
    
    writer.writerow(header)
    writer.writerows(list(zip(*data)))




# B
name = 'rianna' # input('Enter player name: ')
score = '120'   # input('Enter score: ')

with open('scores.csv','r+', newline='') as f:
    reader = list(csv.reader(f))     # read data and convert to list

    data = list(zip(*reader))        # select data excluding headers and transpose

    names = list(data[1])            # create lists for names and scores and add new entry  
    names.append(name)
    scores = list(data[2])
    scores.append(score)
    scores = [float(s) for s in scores]                 # convert to numerical
    
    ordered = sorted(zip(scores, names), reverse=True)  # sort using score
    scores = [i[0] for i in ordered]                    # sorted names
    names = [i[1] for i in ordered]                     # sorted scores 
    places = list(range(1, len(names)+1))               # new places list
    
    data = list(zip(places, names, scores))             # transpose rows to columns  

    f.seek(0)                                           # go to start of file
    writer = csv.writer(f)                              # write data
    writer.writerows(data)
          


    






    
    
    
    
    
    

        

        

        
        
    
        
    
 
    
 
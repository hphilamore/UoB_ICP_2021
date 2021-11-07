 # Exercises Week 3

# Part 1 : Loops

# 1.1
Words = "Hello World"
for Letter in Words:
    print(Letter)
    
# 1.2 


# 1.5
for (x, y) in enumerate(Words):
    print(x, y)
    
for (x, y) in enumerate(Words.replace(' ','')):
    print(x, y)
    

for w,i in zip(Words, range(len(Words))):
    if w == ' ':
        continue
    print(w, i)
    
# 1.6 
sum = 0
for i in range(1,11):
    sum = sum + 5 * i
print(sum)

# 1.7
F = 10 
for i in range(9,0,-1):
    F *= i
print(F)

# 1.8 
count = 0
for i in range(1, 2000):
    if i**3 > 2000:
        break 
    else:
        count += 1
print(count)
    

# 2.1
Word = "Hello World"
TargetLetter = 'l'
i = 0
while Word[i]!=TargetLetter:
    i += 1
print("Target letter is at position", i)

# 2.2
for (n,l) in enumerate(Word):
    if l == TargetLetter:
        print("Target letter is at position", n)
        
for i in range(len(Word)):
    if Word[i] == TargetLetter:
        print("Target letter is at position", i)
    
# 2.3
print(Word.find('l'))

# 2.6
for (n,l) in enumerate(Word):
    if l == TargetLetter:
        print("Target letter is at position", n)
        break
    
# 3.1 
ans = 0
for i in range(10):
    for j in range(5):
        ans += j**2 * (i + j)
print(ans)   

# # 3.2 
# nums = [100, 1000, 10000]
# pi = 3.141592653589793

# for i in nums: 

#     pi_N = 0
    
#     for n in range(i):
#         pi_N += 8 / ((4*n + 1)*(4*n + 3))
    
#     print(f'N={i}, error= ', abs(pi - pi_N))
    

# print(4*10**-5)
# error = 1
# N = 0
# while error >= 10**-5:
#     N += 1
    
#     pi_N = 0
    
#     for n in range(N):
#         pi_N += 8 / ((4*n + 1)*(4*n + 3))
        
#     error = abs(pi - pi_N)
    
#     print(error)
    
# print( N )  


# 3.3 
count = 2
F_num_0 = 0 
F_num_1 = 1

for maximum in [100, 1_000, 10_000]:

    while(F_num_1 < maximum):
        F_num = F_num_1 + F_num_0
        F_num_0 = F_num_1
        F_num_1 = F_num
        count += 1
    
    print('count=', count-1)
    print('F_num=', F_num_0)


# 3.4
# import random
# A, B = 1, 2 
# count = 0

# while(A != B):
#     count += 1
#     A = random.randint(1, 6)
#     B = random.randint(1, 6)
    
# print(f'Match! (after {count} tries)'  )

# # 3.5
# number = random.randint(1, 100)

# user_guess = 1000

# count = 0

# while user_guess != number:
    
#     count += 1
    
#     user_guess = int(input("guess what number I'm thinking of "))
    
#     if user_guess > number:
#         print("Too high!")
#     if user_guess < number:
#         print("Too low!")
        
# print(f'You got it! You guessed the number {number} in {count} tries.')

# 4.1
A = [1,2]
B = [3,4]

# 4.2
A[0] = 5
print(A)

# 4.3
print(sorted(A))
A.sort()
print(A)

# 4.4
C = [A, B]

# 4.5
for c in C:
    for item in c:
        print(item)
        
    
# 4.6
words = ['in', 'my', 'head', 'i', 'know']#input('input a list of 5 words')

for w in words:
    print(w, '- Word length' , len(w))
    
    
# 4.7 
print([i for i in range(101) if i%2])

print([i for i in range(101) if not i%3])

i = 30
for j in range(i-1, 1, -1):
    #print(j)
    if i/j == int(i/j):
        print(i/j)
        
        

# print(True in [i/j==int(i/j) for j in list(range(i-1, 1, -1))])
# print([True in [i/j==int(i/j) for j in list(range(i-1, 1, -1))] for i in [5, 6, 7]])
# print([[i/j==int(i/j) for j in list(range(i-1, 1, -1))]for i in [5, 6, 7]])
primes = [i for i in list(range(101)) if True not in [i/j==int(i/j) for j in list(range(i-1, 1, -1))]]
print(primes)

# 5.2
FondueIngredients = ('gruyere', 'vacherin')

for i in FondueIngredients: print(i)

Fondue_short = FondueIngredients[:-1]
print(Fondue_short) 

#6.1
#help(set)
    
 
# 6.2 
s1 = {1,2,5,5,8}
s2 = {1,2,4,9,2}
print(s2 & s1, 'union') 

# 6.4
print(4 in s1 and 4 in s2)

# 6.5
print(s1 | s2, 'intersection')
print(s1 - s2, 'difference')
print(s1 ^ s2,'symmetric differnece')

# 6.6 
s1.remove(1)
print(s1)
s1.add(6)
print(s1)

# 7.2
names = {"Jill":21, "Sally":20, "Bob":20, "Harry":21}

# 7.3
print(list(names.keys()))

# 7.4
names['Rachel'] = 19
print(names)

# 7.5 
del names['Bob']
print(names)

# 7.6 
print('Harry' in names.keys())

# 8.1
Mult3 = 'Fizz'
Mult5 = 'Buzz'

limit = int(input('Enter a number: '))

for l in range(1,limit):
    if not l%3 and not l%5:
        print('FizzBuzz')
    elif not l%3:
        print('Fizz')
    elif not l%5:
        print('Buzz')
    else:
        print(l)
        
        



    
    
    

    
    
    
    
    
    



        
    
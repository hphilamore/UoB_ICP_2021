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

# 3.2 
nums = [100, 1000, 10000]
pi = 3.141592653589793

for i in nums: 

    pi_N = 0
    
    for n in range(i):
        pi_N += 8 / ((4*n + 1)*(4*n + 3))
    
    print(f'N={i}, error= ', abs(pi - pi_N))
    

print(4*10**-5)
error = 1
N = 1
while error >= 10**-5:
    pi_N = 0
    
    for n in range(N):
        pi_N += 8 / ((4*n + 1)*(4*n + 3))
        
    error = abs(pi - pi_N)
    
    print(error)
    
    N += 1

print( N-1 )  
    
    



        
    
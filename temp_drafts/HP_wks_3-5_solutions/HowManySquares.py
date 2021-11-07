# How many squares do we have to add up to exceed 1e6?
# (An illustration of a while loop)

cumulativeSum=0
counter=0

while cumulativeSum<1000000:
    counter += 1
    cumulativeSum += (counter**2)
    print(cumulativeSum)

print("The answer is", str(counter))

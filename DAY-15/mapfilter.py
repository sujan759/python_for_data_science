def cube(x):
    return x*x*x
print(cube(3))


l=[4,6,8,22,3,12]
newl=[]
for item in l:
    newl.append(cube(item))
    
print(newl)

newli=list(map(cube,l))
print(newli)

# Filter

from functools import reduce

# list of number 
num=[4,6,2,9,7,3,6,3]
# num=[4,6,2,9,7,3,6,3]
#  calculet the sum  of the num using the reduce function

def mysum (x,y):
    return x+y
sum=reduce(mysum,num)
print(sum)
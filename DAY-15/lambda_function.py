def appl(fx , value):
    return 6 + fx(value)
double=lambda x:x*x
cube=lambda x:x*2 
avg=lambda x,y,z:(x+y+z)/3

print(double(4))
print(cube(4))
print(avg(4,2,5))

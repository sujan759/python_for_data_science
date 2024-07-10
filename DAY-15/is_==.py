a=3
b=6

print(a is b)# exact location of object in memory 
print(a==b)  # value
a=(4,5,6)
b=(4,5,6)
print("tuple:",a is b)# exact location of object in memory 
print(a==b)  # value
a=[32,43]
b=[32,43]
print("list:",a is b)# exact location of object in memory 
print(a==b)  # value
# 
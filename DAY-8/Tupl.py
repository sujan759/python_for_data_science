#Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
tup=(4,43,42,2,4,6,8,23,54,)
print(len(tup))
print(type(tup))
print(tup[0:3])
print(tup[1])
print(tup[-3])
print(tup[2:-3])
if 32 in tup:
    print("yes")
else:
    print("no")
    
#  opretion tuple
contries=('india','englnd','america','rusia')
temp=list(contries)
temp.append('china')  #add item
temp.pop(2)  #remove item
temp[2]='suijarland'  #chang item
contries=tuple(temp)
print(contries)

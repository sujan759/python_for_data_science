l=[21,34,341,14,54,5,6,5]
print(l)
l.append(3) # add ton list
l.sort() # acending oder to sort list
print(l)# final list
l.sort(reverse=True) # decending  oder to sort list
print(l)# final list
l.reverse # print revers
# print(l.index(1))# index 2 element print
print(l.count(2))# count 2 element whow mwny time repit
m=l.copy()# create new list as copy
m[8]=8
l.insert(11,77)
print(l)
m=['sd','dd','dubed']
k=m+l
print(k)
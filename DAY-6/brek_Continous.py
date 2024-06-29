# break ka matlab Lop ko chhud kar nikl jao
for i in range(12):
    if(i==10):
        print("10 X",i+1, '=', 10*(i+1))
        i=i+1
        break
print("brek excute")
# continouse skep itrection
for i in range(12):
    if(i==10):
        print("Skip the itraction")
        continue
    print("10 X",i+1, '=', 10*(i+1))
    i=i+1
print("lop excute")
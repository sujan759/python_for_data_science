def funct1():
    try:
        l=[12,23,32,43,76,65,]
        i=int(input("Enter the index:"))
        print(l[i])
        return 0
    except:
        print('Enter as invalid index')
        return 1
    finally:
        print(" I am allwes excute")
x=funct1()
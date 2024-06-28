# match case used
Marks=float(input('Enter your marks'))
match Marks:
    case _ if Marks >=90:
        print("first class")
    case _ if Marks >=70:
        print("Second class")
    case _ if Marks >=50:
        print("Third class")
    case _ if Marks >=30:
        print("Just pass")
    case _ if Marks >=10:
        print("fail")
#  match case are ussed for switch the case 
# every 
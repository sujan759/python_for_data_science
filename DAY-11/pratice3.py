qustion=[
    ["Which language used create facebook?",'python','java','php','NOT',1],
    ["Which language used create facebook?",'python','java','php','NOT',2],
    ["Which language used create facebook?",'python','java','php','NOT',3],
    ["Which language used create facebook?",'python','java','php','NOT',4],
    
    ["Which language used create facebook?",'python','java','php','NOT',1],
    ["Which language used create facebook?",'python','java','php','NOT',2],
    ["Which language used create facebook?",'python','java','php','NOT',3],
    ["Which language used create facebook?",'python','java','php','NOT',4],
    
    ["Which language used create facebook?",'python','java','php','NOT',1],
    ["Which language used create facebook?",'python','java','php','NOT',2],
    ["Which language used create facebook?",'python','java','php','NOT',3],
    ["Which language used create facebook?",'python','java','php','NOT',4],
    
    ["Which language used create facebook?",'python','java','php','NOT',1],
    ["Which language used create facebook?",'python','java','php','NOT',2],
    ["Which language used create facebook?",'python','java','php','NOT',3],
    ["Which language used create facebook?",'python','java','php','NOT',4],
    
]
levels=[1000,4000,6000,8000,10000,15000,20000,31000,100000,2000000,5000000,10000000]
money=0
for i in range(0,len(qustion)):
    qustion= qustion[i]
    print(f"Qustion for Rs. {levels[i]}")
    print(f"a.{qustion[1]}    b.{qustion[2]}")
    print(f"c.{qustion[3]}    d.{qustion[4]}")
    reply=int(input("Enter you answare:"))
    if(reply == qustion[-1]):
        print(f"Corect answer, you have won Rs.{levels[i]}")
        if(i== 4):
            money=1000
        elif(i== 9):
            money=100000
        elif(i== 12):
            money=10000000
    else:
        print("Worng anser!")
        break
print(f"You takes home  mony is Rs. {money} ")
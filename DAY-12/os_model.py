import os
# if(not os.path.exists("DAY-12")):
#     os.mkdir("DAY-12")

# for i in range(0,5):
#     os.mkdir(f"DAY-12/ fill{i+1}")
    
folders=os.listdir("DAY-12")
print(folders)
    
for folder in folders:
    print(os.listdir(f"DAY-12/{folder}"))
    

# creat folder and fill red

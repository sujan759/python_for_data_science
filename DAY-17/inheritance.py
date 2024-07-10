#  in heritance 
class Employee:
    def __init__(self,name,id) :
        self.name=name
        self.id=id
    def showDetailsh(self):
        print(f" The name of Employee : {self.name} is {self.id}")
class programer (Employee):
    def showLanguafge(self):
        print("First language python")

e=Employee("Suajn",23)
e.showDetailsh()
# e .showLanguafge()
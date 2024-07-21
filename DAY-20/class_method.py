class Employee:
    company="google"
    def show(self):
        print(f"The ame of Compane '{self.company}' employee name '{self.name}'")
    
    def changecompany(cls,newcompany):
        cls.company=newcompany
e1=Employee()
e1.name="sujan"
e1.show()

e1.changecompany("apple")
e1.show()

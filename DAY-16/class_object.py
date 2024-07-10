# object orinted program
class Person:  # user def part is class 
    name="sujan"
    occupetion="datascince"
    networth="23cr"
    def info(self):# self parameter reference to the curent instence of the class objectn used to accses variable  that belongs to the class
         
        print(f"{self.name},is a {self.occupetion}")
a=Person()
a.name="rama"
a.occupetion='dms'
print(a)
a.info()



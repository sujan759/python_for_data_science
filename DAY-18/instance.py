class Employe:
    comp="sz service"  # classs 
    def __init__(self,name) -> None:  # instence of class 
        self.name=name
        self.raise_amount=0.9
        
    def showDtailsh(self):
        print(f" The name of employe is '{self.name}' and the raise amount ''{self.raise_amount}'' in {self.comp}")
        
    
    
#  instance of class allwes change posible 
emp1=Employe("sujan")
emp1.raise_amount=2
emp1.showDtailsh()
#  static method 

class math:
    def __init__(self, num) -> None:
        self.num= num

    def addition(self,n):
        self.num=n
    
    @staticmethod
    def add(a,b):
        return a+b
    
a=math(6)
print(a.num)
a.addition(9)
print(a.num)
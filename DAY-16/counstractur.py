# Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.
class Person:
    def __init__(self,a,b) -> None:
        print("hey I am  lerned")
        self.name=a
        self.occ=b
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
c=Person('sujan','datascince')
#  her crete duplicate object
c.info()
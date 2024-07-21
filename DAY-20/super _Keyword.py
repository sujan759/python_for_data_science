class ParentClass:
    def parent(self):
        print("This is the  parent class methode ")
class childeClass(ParentClass):
    def child(self):
        print("This is the  child class methode ")
        
        super().parent()
child_object=childeClass()
child_object.child()
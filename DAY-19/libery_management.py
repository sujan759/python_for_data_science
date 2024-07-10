#  crete a sfotwer libere management
class Library:
    def __init__(self,nobooks) -> None:
        self.nobooks=nobooks
        self.books=[]
        
    def addbook(self,books):
        self.books.append(books)
        self.nobooks=len(self.books)
        
    def showinfo(self):
        print(f"The library has '{self.nobooks}' books . The books are")
        for books in self.books:
            print (books)
            
            
l1 = Library()
l1.addbook("story rider")
l1.addbook("math")
l1.addbook("python")
l1.addbook("dld")
l1.showinfo()

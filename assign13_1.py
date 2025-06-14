class BookStore:
    Noofbooks=0
    def __init__(self,name,author):
        
        self.name=name
        self.author=author
        BookStore.Noofbooks+=1

    def Display(self):
        print("book name is=",self.name)
        print("author name=",self.author)        
        print("number of books",BookStore.Noofbooks)

    
obj1=BookStore("Linux system Programming","Robert Love")
obj1.Display()
obj2=BookStore("c programming","Dennis Ritche")
obj2.Display()






    

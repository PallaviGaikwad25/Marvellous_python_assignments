class Book:
    def __init__(self, bname, price):
        self.bname = bname
        self.__price = 0.0
        self.set_price(price)  

   
    def get_price(self):
        return self.__price

   
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price. Must be greater than 0. Price not updated.")

    
    def display_info(self):
        print("book title is",self.bname)
        
        print("Book Price : ",self.get_price())


def main():
   
    print("Enter book title:")
    bname = input()

    print("Enter book price:")
    price = float(input())

   
    book = Book()
    book.bname
    book.__price

    
    book.display_info()

    print("\nEnter new price to update:")
    new_price = float(input())
    book.set_price(new_price)

    print("\nUpdated Book Details:")
    book.display_info()


if __name__ == "__main__":
    main()

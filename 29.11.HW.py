class Book:
    def __init__(self,book_name,book_price,book_author):
        self.book_name=book_name
        self.book_price=book_price
        self.book_author=book_author
    def displaybook(self):
        print(f"Book_Name:{book_name}\nBook_Price:{book_price}\nBook_Autor:{book_author}")
class Members:
    def __init__(self,member_name,member_ID):
        self.member_name=member_name
        self.member_ID=member_ID
    def displaymembers(self):
        print(f"Member_Name:{member_name}\nMember_ID:{member_ID}")
class Management(Book,Members):
    def __init__(self,book_name,book_price,book_author,member_name,member_ID):
        Book.__init__(self,book_name,book_price,book_author)
        Member.__init__(self,member_name,member_ID)
    def displaymanagementINFO(self):
        self.displaybook()
        self.displaymembers()
a=Management("TITANIC",$4000,"Jack","Bujji",2345)
a.displaymanagementINFO()
        
        

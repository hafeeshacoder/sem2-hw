#1
class User:
 def _init_(self,username,password):
     self.__username=username
     self.__password=password
 def get_username(self):
     return self.__username
 def get_password(self):
     return self.__password
 def set_username(self):
     self.__username=username
 def set_password(Self):
     self.__password=password
 def checkpassword(self):
     digit=False
     char=False
     if len(self.__password)<8:
         return False
     if any (i.isdigit() for i in self.__password): #acgshdn17w
         digit=True
     if any (not i.isalnum() for i in self.__password):
         char=True

     if digit and char:
         print("password is valid")
         return True
     else:
       
          return False
username=input("Enter the username")
password=input("Enter the password:")
u=User(username,password)
if u.checkpassword():
 print(f"Username:{u.get_username()}\nPassword:{u.get_password()}")
else:
 print("Invalid credentials")

 


#Encapsulation with Validation


class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self.set_price(price)
        self.set_stock(stock)

    def set_price(self, price):
        if price <= 0:
            print("Price must be greater than 0")
        self._price = price

    def set_stock(self, stock):
        if not (stock, int) or stock < 0:
            print("Stock must be a non-negative integer")
        self._stock = stock

    def get_stock(self):
        return self._stock
product = Product("Laptop", 999.99, 10)
print(product._name)  
print(product._price)  
print(product.get_stock())  


#Basic Getter and Setter


class Student:
    def __init__(self, name, age, marks):
        self.set_name(name)
        self.set_age(age)
        self.set_marks(marks)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        if not 5 <= age <= 100:
            print
            ("Age must be between 5 and 100")
        self._age = age

    def get_age(self):
        return self._age

    def set_marks(self, marks):
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100")
        self._marks = marks

    def get_marks(self):
        return self._marks

student = Student("John Doe", 20, 85)
print(student.get_name())  
print(student.get_age())  
print(student.get_marks())  



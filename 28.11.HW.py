1. Write a Python program that demonstrates single inheritance. Create a parent class called Person with 
an attribute name and a method show_name to display the name. Create a child class called Student 
that inherits from the Person class and adds a new attribute student_id with a method 
show_student_id to display the student ID. Create an object of the Student class, and use it to display 
both the name and student ID.

class Parent:
    def getn(self):
        self.name=input("Enter your name:")
class Student(Parent):
    def getdetail(self):
        self.ID=int(input("Enter student ID:"))
    def show(self):
        self.getn()
        print(f"Parent Name:{self.name}\nStudent_ID:{self.ID}")
s=Student()
s.getdetail()
s.show()                 
print("________________________________________________________________________________")


2. Write a Python program to demonstrate single inheritance. Create a parent class Employee with 
attributes name and salary, and a method display_details to show the employee's details. Create a 
child class Manager that inherits from Employee and adds an attribute department, along with a 
method display_department to show the department name. Create an object of the Manager class to 
display all details.
class Employee:
    def geta(self):
        self.name=input("Enter your name:")
        self.salary=int(input("Enter your salary"))
class Manager(Employee):
    def getb(self):
        self.deparment=input("Enter your deparment:")
    def show(self):
        self.geta()
        print(f"Name of the Empolyee:{self.name}\nEmployee salary:{self.salary}\nEmployee deparment:{self.deparment}")
m=Manager()
m.getb()
m.show()

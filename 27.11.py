name=input("Enter your name:") 
roll_no=int(input("Enter your roll number:")) 
a=int(input("Enter the marks obained in subject 1:")) 
b=int(input("Enter the marks obtained in subject 2:")) 
c=int(input("Enter the marks obtained in subject 3:")) 
tot=a+b+c 
per=(tot/300)*100 
if per>=85: 
    print("Grade S") 
elif per>=75: 
    print("Grade A") 
elif per>=65: 
    print("Grade B") 
elif per>=55: 
    print("Grade C") 
elif per>=50: 
    print("Grade D") 
else: 
    print("Fail") 
print("******************************************************************") '''

class Student: 
    def __init__(self, name, age, course, grade): 
        self.name =name 
        self.age = age 
        self.course = course 
        self.grade = grade
    def show(self): 
       print(f"Name: {self.name}") 
       print(f"Age: {self.age}") 
       print(f"Course: {self.course}") 
       print(f"Grade: {self.grade}")
    def __del__(self):
        print("All the Details are deleted")
student1 = Student("Hafeesha", 18, "AI", "A") 
student1.show()
del student1
student1.show()

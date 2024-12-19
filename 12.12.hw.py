import random
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def gen_rand_id(self):
        s_id = random.randint(1000, 9000)
        return f"STU{s_id}"

    def verify_id(self):
        student_id = input("Enter student ID: ")
        student_len = len(student_id)
        if student_len == 7:
            if student_id.startswith("STU"):
                if student_id[3:].isdigit():
                    print("Valid")
                    return student_id
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    def verify_name(self):
        name = input("Enter name: ")
        name_len = len(name)
        if name_len >= 2 and  name.replace(" ", "").isalpha():
            print("Valid")
            return name
        else:
            print("Invalid")

    def calculate_grade(self):
        self.a = int(input("Enter marks obtained in subject 1: "))
        self.b = int(input("Enter marks obtained in subject 2: "))
        self.c = int(input("Enter marks obtained in subject 3: "))
        self.d = int(input("Enter marks obtained in subject 4: "))
        self.e = int(input("Enter marks obtained in subject 5: "))
        tot = self.a + self.b + self.c + self.d + self.e
        per = (tot / 500) * 100
        if per >= 80:
            print("1st Grade")
        elif per >= 70:
            print("2nd Grade ")
        elif per >= 60:
            print("3rd Grade")
        elif per >= 40:
            print("4th Grade")
        else:
            print("5thGrade")
    def ver_grade(self):
        while True:
            number = int(input("Enter the grade number (1-12): "))
            if 1 <= number <= 12:
                if number == 1:
                    print(f"{number}st grade")
                elif number == 2:
                    print(f"{number}nd grade")
                elif number == 3:
                    print(f"{number}rd grade")
                elif number==4:
                    print(f"{number}th grade")
                elif number==5:
                    print(f"{number}th grade")
                elif number==6:
                    print(f"{number}th grade")
                elif number==7:
                    print(f"{naumber}th grade")
                elif number==8:
                    print(f"{number}th grade")
                elif number==9:
                    print(f"{number}th grade")
                elif number==10:
                    print(f"{nuumber}th grade")
                elif number==11:
                    print(f"{number}th grade")
                elif number==12:
                    print(f"{number}th grade")
                break
            else:
                print("Invalid grade number. Please enter a number between 1 and 12.")



student = Student("","","")
print("Generated Student ID:", student.gen_rand_id())
student_id = student.verify_id()
name = student.verify_name()
student.calculate_grade()
student.ver_grade()


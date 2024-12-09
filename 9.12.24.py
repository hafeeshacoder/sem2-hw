class Camera:
    def __init__(self,resolution):
        self.resolution=resolution
    def Photo(self):
        print(f"Take a photo{self.resolution}")
class Phone:
    def __init__(self,phone_number):
        self.phone_number=phone_number
    def call(self):
        print(f"Make call to {self.phone_number}")
class Smart_phone(Camera,Phone):
    def __init__(self,brand,model,resolution,phone_number):
        Camera.__init__(self,resolution)
        Phone.__init__(self,phone_number)
        self.brand=brand
        self.model=model
    def show(self):
        print(f"Brand{self.brand}\nModel{self.model}")
s=Smart_phone("Apple","IPhone",13,123456789)
s.Photo()
s.call()
s.show()
print("******************************************************************")        

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def student_info(self):
        print(f"Name: {self.name}\nCourse: {self.course}")
class Student_athlete(Student):
    def __init__(self, name, course, sport):
        Student.__init__(self, name, course)
        self.sport = sport
    def display_athlete_info(self):
        self.student_info()
        print(f"Sport: {self.sport}")
student_athlete = Student_athlete("Hafeesha", "AI", "FOOTBALL")
student_athlete.student_info()
student_athlete.display_athlete_info()


class Person:
    def __init__(self):
        self.name=input("Enter name")
        self.age=int(input("Enter age"))

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.sid=input("Enter student ID:")

class Teacher(Person):
    pass


class Academic():
    def __init__(self):
        self.sub=input("Enter subject:")
        self.marks=eval(input("Enter marks:"))  
class Sports():
    def __init__(self):
        self.sport_name=input("Enter sport name:")
        self.level=input("Enter level:")

class AllRounderStudents(Student,Academic,Sports):

    def __init__(self,isAcademic=False,isSports=False):
        
        self.isAcademic=isAcademic
        self.isSports=isSports
        Student.__init__(self)
        if self.isAcademic:
            Academic.__init__(self)
        if self.isSports:
            Sports.__init__(self)
    def display(self):
        if self.isAcademic and self.isSports:
            print("Allarounder Student Details:")
            print("Name:", self.name)
            print("Age:", self.age)
            print("Student ID:", self.sid)
            print("Subject:", self.sub)
            print("Marks:", self.marks)
            print("Sport Name:", self.sport_name)
            print("Level:", self.level)
        elif self.isAcademic:
            print("Academic Student Details:")
            print("Name:", self.name)
            print("Age:", self.age)
            print("Student ID:", self.sid)
            print("Subject:", self.sub)
            print("Marks:", self.marks)
        elif self.isSports: 
            print("Sports Student Details:")
            print("Name:", self.name)
            print("Age:", self.age)
            print("Student ID:", self.sid)
            print("Sport Name:", self.sport_name)
            print("Level:", self.level)
        else:
            print("Stusdent details:")
            print("Name:", self.name)
            print("Age:", self.age)
            print("Student ID:", self.sid)
obj=AllRounderStudents(isAcademic=True,isSports=True)

obj.display()


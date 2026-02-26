class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,sid):
        super().__init__(name,age)
        self.sid=sid
class Teacher(Person):
    pass
class Academic():
    def __init__(self,sub,marks):
        self.sub=sub
        self.marks=marks
class Sports():
    def __init__(self,sport_name,level):
        self.sport_name=sport_name
        self.level=level
class AllRounderStudents(Student,Academic,Sports):

    def __init__(self,name,age,sid,sub=None,marks=None,sport_name=None,level=None,isAcademic=False,isSports=False):
        Student.__init__(self,name,age,sid)
        self.isAcademic=isAcademic
        self.isSports=isSports
        if isAcademic:
            Academic.__init__(self,sub,marks)
        if isSports:
            Sports.__init__(self,sport_name,level)
    def display(self):
        print("Allarounder Student Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.sid)
        if self.isAcademic :
            print("Subject:", self.sub)
            print("Marks:", self.marks)

        if self.isSports:
            print("Sport Name:", self.sport_name)
            print("Level:", self.level)
        

obj=AllRounderStudents(name="Sushanta Pal",age=21,sid="S123",sub="Math",marks=85,sport_name="Football",level="State",isAcademic=False,isSports=True)
obj.display()
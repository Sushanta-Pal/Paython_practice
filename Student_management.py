class Person:
    def __int__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,sid):
        super().__init__(name,age)
        self.sid=sid
class Teacher(Person):
    pass


class Academic(Student):
    
    def __init__(self,name,age,sid,sub,marks):
        super().__init__(name,age,sid)
        self.sub=sub
        self.marks=marks
class Sports(Student):
    def __init__(self,name,age,sid,sport_name,lavel):
        super().__init__(name,age,sid)
        self.sport_name=sport_name
        self.lavel=lavel

class AllRounderStudents(Academic,Sports):

    def __init__(self, name, age, sid,sub, marks,sport_name,lavel):
        Sports.__init__(self,name,age,sid,sport_name,lavel)
        Academic.__init__(self,name,age,sid,sub,marks)

obj1=AllRounderStudents("Sushanta",21,"S001","Maths",85,"Cricket","Intermediate")

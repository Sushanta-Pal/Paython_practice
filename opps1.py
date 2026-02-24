class Ten:
    def __init__(self, name, dob,address,result):
        self.name=name
        self.dob=dob
        self.address=address
        self.result=result
    def display(self):
        print(f"{self.name}  {self.dob} {self.address}  {self.result}")

class HS(Ten):
    def __init__(self, name, dob,address,result,hsres,domain):
        super().__init__(name,dob,address,result)
        self.hsres=hsres
        self.domain=domain
    def display(self):
        super().display()
        print(f"{self.hsres}  {self.domain}")
class Btech(HS):
    def __init__(self, name, dob, address, result, hsres, domain,clg):
        super().__init__(name, dob, address, result, hsres, domain)
        self.clg=clg
    def display(self):
        super().display()
        print(self.clg)


obj=HS("Sushanta Pal","03-05-2004","Haldia",85.9,73.5,"Science")
obj.display()
obj1=Btech("Sushanta Pal","03-05-2004","Haldia",85.9,73.5,"Science","HIT")
obj1.display()

    

    
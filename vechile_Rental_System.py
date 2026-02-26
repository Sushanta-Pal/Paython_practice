class Vehicle:
    def __init__(self):
        self.v_id=eval(input("Enter vechile id"))
        self.brand=input("enter brand")
        self.name=input("Enter vachile name")
    def calculate_reant(self):
        print(f"{self.name} require $0")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price_per_day=eval(input("Enter price per day for car"))
        self.day=eval(input("For how many days u require the car"))
    def calculate_reant(self):
        print(f"{self.name} require ${self.price_per_day *self.day} for this car")
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.price_per_hour=eval(input("Enter price per hour for Bike"))
        self.hour=eval(input("For how many hour u require the Bike"))
    def calculate_reant(self):
        print(f"{self.name} require ${self.price_per_hour *self.hour} for this bike")   

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.price_per_km=eval(input("Enter price per km for Truck"))
        self.distance=eval(input("For how many km u require the Truck"))
    def calculate_reant(self):
        print(f"{self.name} require ${self.price_per_km *self.distance} for this Truck")
c1=Car()
c1.calculate_reant()
b1=Bike()
b1.calculate_reant()
t1=Truck()
t1.calculate_reant()






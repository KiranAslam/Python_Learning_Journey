#Task 1
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating!")
    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(Animal):
    def bark(self):
        print(f"{self.name} says: woof woof!")
class cat(Animal):
    def meow(self):
        print(f"{self.name} says: meow meow!")


my_dog=dog("shero")
my_dog.bark()
my_dog.eat()
my_dog.sleep()

my_cat=cat("mano")
my_cat.eat()
my_cat.meow()
my_cat.sleep()

#Task 2 (understanding Super keyword)

class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def start(self):
        print(f"The {self.brand} Vehicle is starting")

class Car(Vehicle):
    def __init__(self,brand,year,fuel_type):
        super().__init__(brand,year)
        self.fuel_type=fuel_type
    def show_info(self):
        print(f"Brand:{self.brand} , year:{self.year} , fuel:{self.fuel_type}")
    def drive(self):
        print(f"The {self.brand} car is driving!")

class Motorcycle(Vehicle):
    def wheelie(slef):
        print(f"The motorcycle is doing a wheelie!")

Car1=Car("Toyota",2024,"Hybrid")
Car1.show_info()
Car1.start()
Car1.drive()

Motorcycle1=Motorcycle("Honda",2023)
Motorcycle1.start()
Motorcycle1.wheelie()

#Task 3 (Mutilevel Inheritence)

class Device:
    def __init__(self,brand):
        self.brand=brand
    def power_on(self):
        print("The device is now ON!")
class Computer(Device):
    def __init__(self,brand,ram):
        super().__init__(brand)
        self.ram=ram
    def load_os(self):
        print("The Operating System is Loading!")
class Leptop(Computer):
    def __init__(self,brand,ram,battery_life):
        super().__init__(brand,ram)
        self.battery_life=battery_life
    def show_status(self):
        print("===Devie Info===")
        print(f"Brand:{self.brand} , Ram:{self.ram} , Battery_life:{self.battery_life}.")

my_leptop=Leptop("HP",16,"4h")
my_leptop.power_on()
my_leptop.load_os()
my_leptop.show_status()

my_computer=Computer("Dell", 8)
my_computer.load_os()
my_computer.power_on()

#Task 4 (Multiple Inheritence)

class LandVehicle:
    def __init__(self,brand):
        self.brand=brand
    def drive(self):
        print("Driving on the road!")
class AerialVehicle():
    def __init__(self,max_altitude):
        self.max_altitude=max_altitude
    def fly(self):
        print(f"Fly in the sky at {self.max_altitude} feet!")
class Fly_car(LandVehicle,AerialVehicle):
    def __init__(self,brand,max_altitude):
        LandVehicle.__init__(self,brand)
        AerialVehicle.__init__(self,max_altitude)
    def show_capabilities(self):
        print(f"====capabilities of {self.brand}====")
        self.drive()
        self.fly()

my_future_car=Fly_car("tesla-Air",10000)
my_future_car.show_capabilities()

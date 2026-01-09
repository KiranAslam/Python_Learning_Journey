#Task 01

class Shape:
    def calculate_area(self):
        print("Calculating area for a generic shape.")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        area=3.14*(self.radius**2)
        print(f"Circle Area (Radius {self.radius}): {area}")
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def calculate_area(self):
        area=self.side*self.side
        print(f"Square Area (Side {self.side}): {area}")

shapes_lists=[Square(10),Circle(3),Circle(6),Shape()]
for shape in shapes_lists:
    shape.calculate_area()

#Task 02
class payment:
    def process_payment(self,amount):
        self.amount=amount
        print(f"Processing generic payment of {amount}...")
class creditcard(payment):
    def process_payment(self,amount):
        fee=amount*0.02
        total_amount=amount+fee 
        print(f"paid {total_amount} with 2% fee.")
class easypaisa(payment):
    def process_payment(self,amount):
        fee=10
        total_amount=fee+amount
        print(f"paid {total_amount}  with 10rs fee.")   
    
p1=payment()
c1=creditcard()
e1=easypaisa()
p1.process_payment(700)
c1.process_payment(500)
e1.process_payment(600)

#Task 03
class Employee:
    def do_work(self):
        print("Employee is doing generic work......")
class developer(Employee):
    def do_work(self):
        print("Developer is writing code and fixing bugs.")
class manager(Employee):
    def do_work(self):
        print("Manager is planning projects and attending meetings.")
class designer(Employee):
    def do_work(self):
        print("Designer is creating UI/UX layouts.")

Employee_lists=[developer(),manager(),designer(),developer()]
for e in Employee_lists:
    e.do_work()


# Task 04
class Notification:
    def send(self,message):
        self.message=message
        print(f"Generric Message: {message}")
class Email(Notification):
    def __init__(self,email_address):
        self.email_address=email_address
    def send(self,message):
        print(f"sending email to {self.email_address} : {message}")
class  SMS(Notification):
    def __init__(self,phone_number):
        self.phone_number=phone_number
    def send(self,message):
        print(f"sending SMS to {self.phone_number} : {message}")
class  Whatsapp(Notification):
    def __init__(self,phone_number):
        self.phone_number=phone_number
    def send(self,message):
        print(f"sending Whatsapp to {self.phone_number} : {message}")

e1=Email("kiranaslamsgr@gmai.com")
s1=SMS("03168639430")
w1=Whatsapp("03782682983")
n1=Notification()
msg="your order is ready!"
Notification_lists=[e1,s1,w1,n1]
for i in Notification_lists:
    i.send(msg)

#Task 05

class SmartDevice:
    def __init__(self,name):
        self.name=name
    def turn_on(self):
        print("Device is powering Up........")
    def Device_info(self):
        print("===Device Info===")
        print("General Smart Device.")

class SmartLight(SmartDevice):
    def __init__(self,name,brightness):
        self.brightness=brightness
        super().__init__(name)
    def turn_on(self):
        print(f"Light {self.name} is ON with {self.brightness}% Brightness.")
    def Device_info(self):
        print("===Device Info===")
        print(f"Name:{self.name},Type:Lighting System, Birghtness:{self.brightness} ")

class SmartAC(SmartDevice):
    def __init__(self,name,temp):
        self.temp=temp
        super().__init__(name)
    def turn_on(self):
        print(f"AC {self.name} is cooling at {self.temp}°C.")
    def Device_info(self):
        print("===Device Info===")
        print(f"Name:{self.name},Temperature:{self.temp},Type:climate change")

class SmartTV(SmartDevice):
    def __init__(self,name,channel):
        self.channel=channel
        super().__init__(name)
    def turn_on(self):
        print(f"TV {self.name} is playing channel {self.channel}.")
    def Device_info(self):
        print("===Device Info===")
        print(f"Name: {self.name},channel:{self.channel},Type: Entertainment System")


L1=SmartLight("Tube Light","60")
L2=SmartLight("Bulb","60")
AC1=SmartAC("Hire","30")
AC2=SmartAC("Dawlance","15")
TV1=SmartTV("Dell","JEO News")
D1=SmartDevice("Leptop")
D2=SmartDevice("Drone")
my_home_devices=[L1,L2,AC1,AC2,TV1,D1,D2]
for device in my_home_devices:
    device.Device_info()
    device.turn_on()
    print("-------------------------------")
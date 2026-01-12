#Logistics management system
class Package:
    def __init__(self, tracking_id, weight):
        self.tracking_id = tracking_id
        self.weight = weight 
        self._base_rate = 100 
    def calculate_cost(self):
        return self.weight * self._base_rate
class StandardDelivery(Package):
    def calculate_cost(self):
        cost = (self.weight * self._base_rate) + 50
        print(f"Standard Shipping [{self.tracking_id}]: Rs.{cost}")
        return cost
class ExpressDelivery(Package):
    def calculate_cost(self):
        cost = (self.weight * self._base_rate) * 2
        print(f"Express Shipping [{self.tracking_id}]: Rs.{cost} (Next Day Delivery)")
        return cost
class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.__address = address 
        self.__phone = phone     

    def show_delivery_label(self):
        print(f"--- DELIVERY LABEL ---")
        print(f"Recipient: {self.name}")
        print(f"Address: {self.__address}") 
        print(f"-----------------------")
cust1 = Customer("Kiran", "New Humna Hostel Phase I ", "031693809")
pkg1 = StandardDelivery("STD-990", 2.5) 
pkg2 = ExpressDelivery("EXP-112", 1.5)  
cust1.show_delivery_label()
shipments = [pkg1, pkg2]
print("Calculating Shipping Costs:")
for item in shipments:
    item.calculate_cost()
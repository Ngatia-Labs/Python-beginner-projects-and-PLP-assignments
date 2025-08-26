# Assignment 1: Smartphone Example 🏗️

# Parent class (Device)
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class (Smartphone) inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # inheritance
        self.storage = storage
        self.__battery = battery         # encapsulation (private)

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}...")

    def charge(self, amount):
        self.__battery += amount
        print(f"🔋 Battery charged to {self.__battery}%")

    def get_battery(self):
        return self.__battery

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 75)
phone2 = Smartphone("Apple", "iPhone 15", "512GB", 50)

# Using methods
phone1.make_call("+254702101264")
phone2.charge(30)

print("Battery Level:", phone1.get_battery())
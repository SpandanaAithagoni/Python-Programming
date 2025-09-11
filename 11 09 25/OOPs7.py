from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, license_plate, owner):
        self.__license_plate = license_plate   
        self.__owner = owner                   
    
    def get_license_plate(self):
        return self.__license_plate
    
    def get_owner(self):
        return self.__owner
    
    def set_owner(self, new_owner):
        self.__owner = new_owner
    
    def display(self):
        print("Generic Vehicle")
    
    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, license_plate, owner, helmet_required=True):
        super().__init__(license_plate, owner)
        self.helmet_required = helmet_required
    
    def display(self):
        print(f"Bike - Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, Helmet Required: {self.helmet_required}")
    
    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, license_plate, owner, seats=4):
        super().__init__(license_plate, owner)
        self.seats = seats
    
    def display(self):
        print(f"Car - Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, Seats: {self.seats}")
    
    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, license_plate, owner, four_wheel_drive=True):
        super().__init__(license_plate, owner)
        self.four_wheel_drive = four_wheel_drive
    
    def display(self):
        print(f"SUV - Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, 4WD: {self.four_wheel_drive}")
    
    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, license_plate, owner, max_load_capacity=10000):
        super().__init__(license_plate, owner)
        self.max_load_capacity = max_load_capacity
    
    def display(self):
        print(f"Truck - Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, Max Load: {self.max_load_capacity}kg")
    
    def calculate_parking_fee(self, hours):
        return 100 * hours


class ParkingSpot:
    def __init__(self, spot_id, size):
        self.__spot_id = spot_id
        self.__size = size        
        self.__is_occupied = False
        self.__vehicle = None

    def get_spot_id(self):
        return self.__spot_id
    
    def is_occupied(self):
        return self.__is_occupied
    
    def get_size(self):
        return self.__size
    
    def get_vehicle(self):
        return self.__vehicle
    
    def assign_vehicle(self, vehicle):
        if self.__is_occupied:
            return False
        
        if isinstance(vehicle, Bike) and self.__size in ["S", "M", "L", "XL"]:
            pass
        elif isinstance(vehicle, Car) and self.__size in ["M", "L", "XL"]:
            pass
        elif isinstance(vehicle, SUV) and self.__size in ["L", "XL"]:
            pass
        elif isinstance(vehicle, Truck) and self.__size == "XL":
            pass
        else:
            return False
        
        self.__vehicle = vehicle
        self.__is_occupied = True
        return True
    
    def remove_vehicle(self):
        if not self.__is_occupied:
            return None
        vehicle = self.__vehicle
        self.__vehicle = None
        self.__is_occupied = False
        return vehicle
    
class ParkingLot:
    def __init__(self):
        self.spots = []
    
    def add_spot(self, spot):
        self.spots.append(spot)
    
    def show_spots(self):
        for spot in self.spots:
            status = "Occupied" if spot.is_occupied() else "Free"
            print(f"Spot {spot.get_spot_id()} ({spot.get_size()}) - {status}")
    
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_occupied() and spot.assign_vehicle(vehicle):
                print(f"Vehicle {vehicle.get_license_plate()} parked in Spot {spot.get_spot_id()} ({spot.get_size()})")
                return True
        print(f"No suitable spot found for Vehicle {vehicle.get_license_plate()}")
        return False
    
    def unpark_vehicle(self, vehicle, hours, payment_method):
        for spot in self.spots:
            if spot.is_occupied() and spot.get_vehicle() == vehicle:
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(f"Parking fee: ₹{fee}")
                payment_method.process_payment(fee)
                return True
        print(f"Vehicle {vehicle.get_license_plate()} not found in lot!")
        return False

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in cash")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Card")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI")

lot = ParkingLot()
lot.add_spot(ParkingSpot(1, "S"))
lot.add_spot(ParkingSpot(2, "M"))
lot.add_spot(ParkingSpot(3, "L"))
lot.add_spot(ParkingSpot(4, "XL"))
    
bike = Bike("AP01AB1234", "Srujana")
car = Car("TS09XY5678", "Ravi")
suv = SUV("KA05MN4321", "Kiran")
truck = Truck("MH12TR9876", "Manoj")
    
lot.park_vehicle(bike)
lot.park_vehicle(car)
lot.park_vehicle(suv)
lot.park_vehicle(truck)
    
print("\n--- Parking Lot Status ---")
lot.show_spots()
    
print("\n--- Unparking ---")
lot.unpark_vehicle(car, 3, UPIPayment())  
lot.unpark_vehicle(truck, 5, CashPayment()) 
    
print("\n--- Final Parking Lot Status ---")
lot.show_spots()


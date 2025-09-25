
class Vehicle:
    def __init__(self, brand, model, max_speed, fuel=100):
        # CONSTRUCTOR with proper attributes
        self.brand = brand
        self.model = model
        self._max_speed = max_speed  # ENCAPSULATION
        self._fuel = fuel
        self._distance = 0  # Private attribute
        self.is_running = False
    
    # METHODS that bring class to life
    def start_engine(self):
        if not self.is_running and self._fuel > 0:
            self.is_running = True
            self._fuel -= 5
            return f"{self.brand} {self.model} engine started! {self._fuel}%"
        return "❌ Cannot start - check fuel or engine status"
    
    def drive(self, km=50):
        if self.is_running:
            fuel_needed = km / 10
            if self._fuel >= fuel_needed:
                self._distance += km
                self._fuel -= fuel_needed
                return f" Drove {km}km | Total: {self._distance}km | {self._fuel:.0f}%"
            return "❌ Not enough fuel!"
        return "❌ Start engine first!"
    
    #  ENCAPSULATION: Getter methods
    def get_info(self):
        return f"{self.brand} {self.model} | Max: {self._max_speed}km/h | ⛽{self._fuel:.0f}%"
    
    def get_distance(self):
        return f"Total distance: {self._distance}km"
    
    def refuel(self):
        self._fuel = 100
        return "⛽ Tank full! 100% fuel"

# INHERITANCE LAYER
class Car(Vehicle):
    def __init__(self, brand, model, max_speed, fuel=100, doors=4):
        super().__init__(brand, model, max_speed, fuel)
        self.doors = doors  #  New attribute
        self._trunk_open = False  # Encapsulation
    
    #  POLYMORPHISM: Different behavior
    def start_engine(self):
        result = super().start_engine()
        if "started" in result:
            return f" CAR: {result} | Doors: {self.doors}"
        return result
    
    def open_trunk(self):
        self._trunk_open = not self._trunk_open
        status = "open" if self._trunk_open else "closed"
        return f" Trunk {status}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, max_speed, fuel=100, type="Sport"):
        super().__init__(brand, model, max_speed, fuel)
        self.type = type  #  New attribute
        self._helmet_on = False  # Encapsulation
    
    # POLYMORPHISM: Different behavior
    def start_engine(self):
        result = super().start_engine()
        if "started" in result:
            return f" MOTORCYCLE: {result} | Type: {self.type}"
        return result
    
    def wear_helmet(self):
        self._helmet_on = True
        return "Helmet secured! Safe to ride"
    
    def drive(self, km=50):  # POLYMORPHISM
        if not self._helmet_on:
            return "⚠️ Wear helmet before driving!"
        return super().drive(km)

# DEMO FUNCTION
def demo():
    print("===  VEHICLE DEMO ===\n")
    
    vehicles = [
        Vehicle("Toyota", "Generic", 180),
        Car("Honda", "Civic", 200, 80, 4),
        Motorcycle("Yamaha", "R1", 300, 90, "Sport")
    ]
    
    for v in vehicles:
        print(v.get_info())
        print(v.start_engine())
        
        if isinstance(v, Car):
            print(v.open_trunk())
        elif isinstance(v, Motorcycle):
            print(v.wear_helmet())
        
        print(v.drive(60))
        print(v.get_distance())
        print(v.refuel())
        print()

# RUN
demo()

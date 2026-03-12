# Ubungen, John Daniel L.
# BCS13
# Class2 Activity

class Car:
    # Class attribute
    def __init__(self, colr, modl, manufac):
        self.colr = colr
        self.modl = modl
        self.manufac = manufac

    def show(self):
        print(f"Color: {self.colr}\nModel: {self.modl}\nManufacturer: {self.manufac}")

# Creating Object
print("Car 1")
carOne = Car(colr="White", modl="RAIZE 1.0 Turbo CVT 2025", manufac="Toyota")  # Instantiation
carOne.show()

print("\nCar 2")
# Modify Object Attributes
carTwo = Car(colr="Brown", modl="GT-R 3.8L-V6-6AT-4WD 2022", manufac="Nissan")  # Instantiation
carTwo.show()  

print("\nCar 3")
# Modify Object Attributes
carThree = Car(colr="Black", modl="Chiron 2022", manufac="Bugatti")  # Instantiation
carThree.show()
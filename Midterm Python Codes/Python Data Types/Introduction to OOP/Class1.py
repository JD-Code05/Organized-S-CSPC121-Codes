#Ubungen, John Daniel L.
#BCS13
#Class1 Activity
class Car:
    #class attribute
    colr = "White"
    modl = "RAIZE 1.0 Turbo CVT 2025"
    manufac = "Toyota"
    
#Creating Object
print("Car 1")

carOne=Car() #instantiation
print("Color",carOne.colr)
print("Model",carOne.modl)
print("Manufacturer",carOne.manufac)


print("\nCar 2")
#Modify Object Attributes
carTwo=Car() #instantiation

carTwo.colr="Brown"
carTwo.modl="GT-R 3.8L-V6-6AT-4WD 2022"
carTwo.manufac="Nissan"

print("Color",carTwo.colr)
print("Model",carTwo.modl)
print("Manufacturer",carTwo.manufac)

print("\nCar 3")
#Modify Object Attributes
carThree=Car() #instantiation

carThree.colr="Black"
carThree.modl="Chiron 2022"
carThree.manufac="Bugatti"

print("Color",carThree.colr)
print("Model",carThree.modl)
print("Manufacturer",carThree.manufac)
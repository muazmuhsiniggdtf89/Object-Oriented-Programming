class Vehicles:

    def __init__(vehicleType):
        print("Vehicle is a ", vehicleType)

class Car(Vehicles):
    def __init__(self):
        Vehicles.__init__('Car')

print(issubclass( Car, Vehicles))

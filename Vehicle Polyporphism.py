class BMW:
    def fuel_type(self):
        print("Fuel Type: Petrol")

    def max_speed(self):
        print("Max Speed: 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Fuel Type: Petrol")

    def max_speed(self):
        print("Max Speed: 340 km/h")



def car_details(car):
    car.fuel_type()
    car.max_speed()
   


bmw_car = BMW()
ferrari_car = Ferrari()


for car in (bmw_car, ferrari_car):
    car_details(car)

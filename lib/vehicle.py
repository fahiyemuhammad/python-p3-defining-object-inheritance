class Vehicle:
    def __init__(self,wheel_size,wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"
     
    def fill_up_tank(self):
        return "filling up!"   

vehicle1 = Vehicle(23,19)
print(vehicle1.fill_up_tank)
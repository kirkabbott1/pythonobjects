# Create a class Vehicle. A Vehicle object will have 3 attributes:
#
# make
# model
# year
#Add a print_info method to the Vehicle class. 

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print self.make, self.model, self.year


car = Vehicle("ford", "f150", 2193)

car.print_info()

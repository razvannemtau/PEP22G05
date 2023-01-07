"""
A production facility needs an iterable object to keep track off car warranty.
Each car have a int serial and datetime object for when he the car was produced
Iterating the object will return all cars that are still covered by 3 years warranty (serial, <timedelta>)
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add sold care
    d) 10p: Method to print cars not covered by warranty
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Call method to add (sell) car (serial, <datetime>))
        - 1588, 20 Jan 2019 10:30:32
        - 1692, 20 Jan 2021 9:20:25
        - 1994, 20 Jan 2022 9:10:30
    c) 10p: Call method to return expired warranty (serial, <datetime>))
    d) 10p: Iterate the created object and write each care covered by warranty in a file
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""
from datetime import datetime

"""creating the Facility Iterator class"""

class FacilityIterator:
    "class for facility iterator"



    """creating the Facility Iterator class"""
    def __init__(self, cars):
        self.cars = self.cars

    def __iter__(self):
        return self

    def __next__(self):
         if self.cars:
             for cars in self.cars.items():
                return cars
         else:
             raise StopIteration

class Facility():
    "class for facility"

    def __init__(self):
        self.cars = {}  # dictionary to collect sold cars

    def add_cars(self, serial, datetime):  # method for adding cars
        self.cars.update({serial: datetime})
        print(self.cars)

    def out_of_warranty(self):  # method for pulling out of warranty cars
        # threeyearwarranty = datetime.now() - datetime(2023, 1, 7, 18, 30, 00)
        # print(threeyearwarranty)
        for key, values in self.cars.items():
            result = datetime.now() - self.cars[key]
            print(result)
            return result

            # res = self.cars[values]
            # print(res)


facility = Facility()
"creating instance of facility"
facility.add_cars(1588, datetime(2019, 1, 20, 10, 30, 32))
facility.add_cars(1692, datetime(2021, 1, 20, 9, 20, 25))
facility.add_cars(1994, datetime(2022, 1, 20, 9, 10, 30))
"calling method to add cars to facility"

print(facility.out_of_warranty(), 'this should be the cars that are out of warranty')
"calling method to show expired warranties"

with open('Exam3.txt', 'w') as file:
    for item in facility.out_of_warranty():
        file.write(str(item) + '\n')
"write each care covered by warranty in a file"

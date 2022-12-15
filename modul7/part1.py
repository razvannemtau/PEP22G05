import time

class Car:
    color = 'yellow'
    motors = ['fw-2kengine']
    lights = 'off'

    def __init__(self, color= 'red'):
        # print(self.color)
        # wheels = 4 # this is local to __init__
        self.wheels = 4
        self.construction_date = time.time()
        self.color = color

    def start_car(self):
        print('car noises')
        self.lights = 'on'


    @staticmethod
    def factorial(number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


    def __eq__(self, other):
        print('ups')
        print(self.construction_date, other.construction_date)
        if self.color == other.color and self.wheels == other.wheels:
            return True
        else:
            return False


    def __str__(self):
        return f'{self.color}, {self.construction_date}, {self.wheels}'

# car1 = Car('tree')
# print(type(car1))
# print(car1.color)
#
# time.sleep(1)
#
# car2 = Car()
# print(type(car2))
# print(car2.color)
#
# car2.color = 'blue'
# print('car1 is ', car1.color)
# print('car2 is ', car2.color)
#
# car2.motors.append('rw-4kengine')
# print('car1 motor is', car1.motors)
# print('car2 motor is', car2.motors)
#
# car2.wheels = 5
# print('car1 wheels is', car1.wheels)
# print('car2 wheels is', car2.wheels)
#
# print('car1 wheels is', car1.construction_date)
# print('car2 wheels is', car2.construction_date)

print(id(Car))
print(type(Car))

car1 = Car()
print(car1.color)
print(Car.__init__(car1, color='magenta'))
print(car1.color)

print('before', car1.lights)
car1.start_car()
print('after', car1.lights)

print('before', car1.lights)
print(Car.start_car(car1))
print('after', car1.lights)

print(Car.factorial(5))
print(car1.factorial(5))

car1 = Car()
car1.wheels = 5
time.sleep(0.1)
car2 = Car()

print(car1 == car2)

print(car1)

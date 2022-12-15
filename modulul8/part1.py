# exception classes
# import time
#
# class MyException(BaseException):
#     def __str__(self, *args, **kwargs):
#         #print(self.args)
#         #print(self.kwargs)
#         return f'{self.args, self.__traceback__}'
#
#
# try:
#     if time.time() > 50000:
#         raise MyException('test', 'test2')
# except Exception:
#     print('Test Exception')
# except MyException as obj1:
#     print(obj1)
#     print('success')
#     raise

# keyboard interrupt should not be treated
# try:
#     while True:
#         sleep(1)
#         print('in loop')
# except KeyboardInterrupt:
#     while True:
#         sleep(1)
#         print('new loop')
# # AttributeError()

#GENERATORS
#
my_generator = range(2)
print(type(my_generator))
my_itterator = my_generator.__iter__()
new_itterator = my_itterator.__iter__()


print(my_itterator.__next__())
# print(next(my_itterator))
print(next(new_itterator))
# print(next(my_itterator))
# print(next(my_itterator))

# def my_generator(number):
#     return ??

class MyIterator():

    def __init__(self, number):
        self.number = number
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == self.number:
            raise StopIteration
        return self.counter

my_itterator = MyIterator(1000000)
print(my_itterator.__next__())
print(my_itterator.__next__())
print(my_itterator.__next__())

new_itterator = my_itterator.__next__()
print(id(new_itterator), id(my_itterator))
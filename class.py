# ## Class Employee wt one object
# class Employee:
#     def display(self):
#         print("Hello my name is AC")

# emp_obj = Employee()
# emp_obj.display()

# ## Class with multiple objects
# class Employee:
#     def display(self):
#         print("Hello my name is Odinaka")

# emp_obj1 = Employee()
# emp_obj1.display()

# emp_obj2 = Employee()
# emp_obj2.display()

# ## Constructor for self parameter
# class Employee:
#     def __init__(self):
#         print("message from constructor")
# emp = Employee()

# ## Constructor wt self parameter
# class Employee:
#     def __init__(self):
#         print("constructor")
    
# emp = Employee()
# emp.__init__()

# ## Constructor wt 1 parameter
# class Employee:
#     def __init__(self, id):
#         self.id = id
#         print("Employee id is:", self.id)
    
# emp1 = Employee(1)
# emp2 = Employee(2)

# ## Constructor wt 2 parameter
# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#     def display(self):
#         print("Hello my id is:", self.id)
#         print("Hello my name is:", self.name)
    
# emp1 = Employee (1, "AC")
# emp1.display()
# emp2 = Employee(2, "Odinaka")
# emp2.display()

## 
# class Student:
#     def m1(self):
#         self.a = 11
#         self.b = 21
#         self.c = 34
#         print(self.a)
#         print(self.b)
#         print(self.c)

# s = Student()
# s.m1()
# print(s.__dict__)


# #Declaring a static variable inside a class and outside of a method
# class Demo:

#     a = 20

#     def m(self):
#         print('This is a method')

# print(Demo.__dict__)

# #Declaring a static variable inside a constructor
# class Demo:
#     def __init__(self):
#         Demo.b = 20     

# print(Demo.__dict__)

# #Declaring a static variable inside instance method
# #Eg 1
# class Demo:
#     def m1(self):
#         Demo.b = 20

# obj = Demo()
# obj.m1()
# print(Demo.__dict__)

# #Eg 2 Static variable by using class method
# class Demo:
#     @classmethod
#     def m2(cls):
#         Demo.b=30

# obj=Demo()
# obj.m2()
# print(Demo.__dict__)

# #Eg 3 Static method by using class name
# class Demo:
#     @staticmethod
#     def m3():
#         Demo.z=10

# Demo.m3()
# print(Demo.__dict__)

# ## DECORATOR PATTERN Eg1
# def hello_decorator(func):
#     def inner1():
#         print("Hello, this is before function execution")
#         func()
#         print("This is after function execution")
#     return inner1

# def function_to_be_used():
#     print("This is inside the fuction!!")

# something = hello_decorator(function_to_be_used)

# something()

# ## Decorator Eg2
# import time
# import math

# def calculate_time(func):
#     def inner1(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print("Total time taken in:", func.__name__, end - begin)
#     return inner1

# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

# ## Local Variable in Python correct eg1
# class Demo:
#     def m(self):
#         a=10 #Local Variable
#         print(a)
# d=Demo()
# d.m()

# ## Local Variable in Python error eg2
# class Demo:
#     def m(self):
#         a=10 #Local Variable
#         print(a)
#     def n(self):
#         print(a)    
# d=Demo()

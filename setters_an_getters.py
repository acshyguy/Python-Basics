# class Customer:
#     def set_name(self, name):
#         self.name = name
#     def set_id(self, id):
#         self.id = id
#     def get_name(self):
#         return self.name
#     def get_id(self):
#         return self.id

# c=Customer()
# c.set_name("Balayya")
# c.set_id(1)
# print(c.name)
# print("My name is:", c.get_name())
# print("My id is:", c.get_id())

## Class Method
# class Pizza:
#     radius=200
#     @classmethod
#     def get_radius(cls):        #cls represents the Pizza class
#         return cls.radius
# print(Pizza.get_radius())

# ## Static Method
# class Demo:
#     @staticmethod
#     def sum(x,y):
#         print(x+y)
#     @ staticmethod
#     def multiply(x,y):
#         print(x*y)
# Demo.sum(2,3)
# Demo.multiply(2,4)

# ## Nested classes
# class A:
#     def __init__(self):
#         print("Outer class object creation")
#     class B:
#         def __init__(self):
#             print("Inner class object creation")
#         def m1(self):
#             print("inner class method")

# a=A()
# b=a.B()
# b.m1()

# ##Garbage Collection
# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())

# ## Single Inheritance
# class A:
#     def m1(self):
#         print("A class m1 Method")
# class B(A):
#     def m2(self):
#         print("Child B is derived from A calss: m2 Method")
# obj = B()
# obj.m1()

# ## Multilevel Inheritance
# class A:
#     def m1(self):
#         print("Parent class A: m1 Method")
# class B(A):
#     def m2(self):
#         print("Child class B derived from A: m2 Method")

# class C(B):
#     def m3(self):
#         print("Child class C derived from B: m3 Method")

# obj = C()
# obj.m1()
# obj.m2()
# obj.m3()

# ## Multiple Inheritance
# class P1:
#     def m1(self):
#         print("Parent 1 Method")
# class P2:
#     def m2(self):
#         print("Parent 2 Method")

# class C(P1, P2):
#     def m3(self):
#         print("Child Method")

# c = C()
# c.m1()
# c.m2()
# c.m3()

# ### Parent class having same name as method
# class P1:
#     def m1(self):
#         print("Parent 1 Method")
# class P2:
#     def m2(self):
#         print("Parent 2 Method")

# class C(P1, P2):
#     def m3(self):
#         print("Child Method")

# c = C()
# c.m2()
# c.m1()

# ## Constructor Overriding
# class P:
#     def properties_status(self):
#         print("Money, Land, Gold")
#     def tp_marry(self):
#         print("Anushka")
# class C(P):
#     def study_status(self):
#         print("Studies done waiting for job")
#     def to_marry(self):
#         print("Megha")

# c = C()
# c.properties_status()
# c.study_status()

# ###
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Employee (Person):
#     def __init__(self, name, age, eno, esal):
#         super().__init__(name, age)
#         self.eno = eno
#         self.esal = esal
#     def display(self):
#         print("Employee Name:", self.name)
#         print("Employee Age:", self.age)
#         print("Employee Number:", self.eno)
#         print("Employee Salary:", self.esal)

# e1 = Employee("Surabhi", 16, 872425, 26000)
# e1.display()
# e2 = Employee("Able", 16, 872426, 36000)
# e2.display()

# ###Abstract Class and Method
# from abc import *    ##Importing all
# class Demo1(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
#     def m3(self):
#         print("Implemented method")

# Demo1()

# ###importing specific abstract class and method
# from abc import ABC, abstractmethod
# class Bank(ABC):      #abstract class
#     def bank_info(self):
#         print("Welcome to bank")
#     @abstractmethod
#     def interest(self):
#         "Abstract Method"
#         pass

# class Access(Bank):         ##Subclass of abstract class
#     def interest(self):
#         "Implementation of abstract method"
#         print("In Access bank N5000 interest")

# s= Access()
# s.bank_info()
# s.interest()

## string method
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def __str__(self):
        return "This is Student object with name {} and roll no {}". format(self.name, self.rollno)
    
s1 = Student("Ram", 10)
s2 = Student("Rahim", 12)
print(s1)
print(s2)
"""
Project - Coffee machine - OOP version.

OOP - Object oriented programming : A programming paradigm that organizes software into classes and objects
OOP model real-word entities like a 'Car', 'Employee', 'People', etc
It groups related data (attributes) and behavior (methods) together.
It makes code reusable, organized and scalable.

"""
# Class      Object
# Blueprint
# Car   -  has    red color, chasis, steering, dashboard, etc   ( attributes)
#           do    - drive, honk, speed,      ( methods)   ( functions)

class Person:
    species = "Human"     # class attribute

    def __init__(myobject, name, age):
        myobject.name = name    # instance attributes
        myobject.age = age

    def greet(abc):
        return "Hello, " + abc.name + "!"

    def welcome(abc):
        message = abc.greet()
        print(message + " Welcome to our website.")

p1 = Person("Michael", 19)
p1.welcome()
print(p1.species)
p2 = Person("Job", 25)
p2.welcome()
print(p2.species)





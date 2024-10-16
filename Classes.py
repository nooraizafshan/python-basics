from multiprocessing.resource_tracker import register


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!



class Patients:
    def __init__(self, name, age, cnic):
        self.name = name
        self.age = age
        self.cnic = cnic

    def registerpatients(self):
        return f'{self.name} is registered, age: {self.age}, cnic: {self.cnic}'

p = Patients('ags', 5, 5555)
print(p.registerpatients())  # Output: ags is registered, age: 5, cnic: 5555






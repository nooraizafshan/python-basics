# Polymorphism and Encapsulation: Advanced OOP Concepts
#
# Polymorphism: The ability to use a unified interface to work with different data types.
#
# Encapsulation: The bundling of data and methods that operate on the data within one unit, typically a class.
#
# Example: Polymorphism


class Bird:
    def speak(self):
        return "Chirp"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())

# Polymorphism in action
bird = Bird()
dog = Dog()

animal_sound(bird)  # Output: Chirp
animal_sound(dog)  # Output: Woof


# Example: Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

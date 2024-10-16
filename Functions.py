# functions
#defining function
from math import trunc
from operator import truth


def Greeting_function():
    print('greetings')
Greeting_function()

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

#arguments and return function
def add(a,b):
    return a+b
    result=add(4,5)
    print(f"The sum is: {result}")


#lambda function

add = lambda a, b: a + b
print(f"The sum using lambda is: {add(5, 3)}")
#
# Defining Functions:
# Write a function called square that takes a number as an argument and returns its square. Test it with a few numbers.

def calc_square():
    number=input('enter number')
    num=int(number)
    num*=num
    print(f"square rooot :{num}")
calc_square()

# Arguments and Return Values
# Write a function called is_even that takes an integer as an argument and returns True if the number is even, and False otherwise.


def is_even(num):
    if num % 2 == 0:
        return 'true'
    else:
        return 'false'

print(is_even(5))  # Test the function



# Write a function called calculate_area that takes the length and width of a rectangle as arguments and returns the area.
def calculate_area(length,width):
    return length * width
area = calculate_area(4,5)
print(f"The area of the rectangle is: {area}")


# Lambda Functions:
# Write a lambda function to calculate the product of two numbers.

product=lambda a,b:a*b
print(product(5,8))

# Write a lambda function that takes a list of numbers and returns the maximum number from the list.
# Lambda function to find the maximum number in a list
find_max = lambda l: max(l)

# List of numbers
numbers = [3, 5, 1, 9, 2]

# Using the lambda function to find the maximum number
print(find_max(numbers))  # Output: 9

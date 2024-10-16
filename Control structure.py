   #1. Conditional Statements: if, elif, and else

#program to build a grade calculator

def grade_checker():
    grade=input('Enter your marks')
    marks=int(grade)

    if marks > 90:
        print('A+')
    elif marks > 80:
        print('A')
    elif marks > 70:
        print('B+')
    elif marks > 60:
        print('B')
    elif marks > 50:
        print('C+')
    else:
        print('fail')

grade_checker()

     #2. Loops: for and while

#Example: Sum of Numbers Using for Loop

def sum_numbers():
    total=0
    for i in range (1,11):
        total+=i
    print(f"The sum of numbers from 1 to 10 is: {total}")
sum_numbers()

#example factorial using while loop

def calc_factorial(n):

    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

number = int(input("Enter a number to find its factorial: "))

print(f"The factorial of {number} is: {calc_factorial(number)}")

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")


#     3.Using break and continue Statements
#Example: break in a Loop
def find_first_multiple_of_5():
    for num in range(1, 101):
        if num % 5 == 0:
            print(f"The first multiple of 5 between 1 and 100 is: {num}")
            break  # Exit the loop as soon as we find the first multiple of 5

find_first_multiple_of_5()

#Example: continue in a Loop

def skip_multiples_of_3():
    for num in range(1, 11):
        if num % 3 == 0:
            continue  # Skip multiples of 3
        print(num)

skip_multiples_of_3()






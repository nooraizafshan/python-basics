#1: Write small programs to declare variables and use different data types

num=3,5
print(num)
name='sidra','said'
print(name)
marks=45.6,56.7
print(marks)


# 2: Write programs that take input from the user and display the output.
name=input('enter your name')
print(name)

# 3:Write a program to convert a string to an integer and perform arithmetic operations.
data=input('enter string ')
print('before converting to string ')
print(data)
print('after converting string to integer')
num=int(data)
print(data)

#Write a program to convert a string to an integer and perform arithmetic operations.
num_str=input('enter num')
number=int(num_str)

sum=number+10
print('sum',sum)


#Write a program that takes two numbers as input and performs all arithmetic operations on them.
num1=input('enter first number ')
n1=int(num1)
num2=input('enter second number ')
n2=int(num2)
sum=n1+n2
print('sum=',sum)

if n1 > n2:
    sub = n1 - n2
    print('Subtraction =', sub)
elif n2 > n1:
    sub = n2 - n1
    print('Subtraction =', sub)
else:
    print('Both numbers are equal; no subtraction to be done')

#Write a program to check if a given number is even or odd using comparison and logical operators.
number=input('enter number')
n=int(number)
if(n%2==0):
    print('even')
else :
    print('odd')


#Write a program to calculate the area of a rectangle. Take the length and width as input from the user and print the area.





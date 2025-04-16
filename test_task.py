#
# 1. You have the following Python code:
# x= input("Enter a number: ")
# print(x * 2)
# (a) Run this code in Interactive Mode and explain the output.
# (b) Save it as a script and run it in Script Mode. What is the difference in behavior?

x=input('enter a number: ')
print(x*2)
'''
(a) in interactive mode we get the output as 22(if x=2), 
this is because the value entered is a string.
(b) in script mode too we will get the same answer because regardless of the mode
the input will be read as a string , to solve this problem we can simply write the following code

'''
x=int(input('enter the number: '))
print(x*2)
#this above code will return the two times of the value entered as intended

'''
2. The following Python code has indentation errors. Fix them without changing the logic:
def greet(name):
print("Hello,", name)
 if name == "Alice":
    print("Welcome back!")
   print("Have a great day!")

greet("Alice")
'''
def greet(name):
    print("Hello,",name)
    if name=="Alice":
        print("Welcome back!")
    print("Have a good day!")
greet("Alice")    


'''
3. What will be the output of the following code? Explain why.

x = 10

def change():
    x = x + 5
    print(x)

change()
'''
x=10#it is a global variable which cannot be accessed inside the defined function
def change():
    x=10 #here the thing is we will get error because no local variable is defined here.
    x=x+5
    print(x)
change()  

'''
4. What will be the output of the following code?
this is a change
x = "5"
y = 2
print(int(x) + y)  # Line 1
print(x + str(y))  # Line 2
print(float(x) + y)  # Line 3
Explain each line’s output and any potential errors that might occur if the data types were changed.

'''
x="5"
y=2
print(int(x) + y)
print(x+ str(y))
print(float(x) + y)
#here the in line 1 we will get the output as 7 
#here in the line 2 we will get the output as 52 
#here in the line 3 we will get the output as 7.0
#any possible error here might be that if we dont
#typecast one variable according to the other we wont
#  get the desired result and we will get the erorr

'''
5. You are given the following function:

def square(n):
    return n * n
Add a proper docstring to this function explaining what it does and its expected input and output.
Write a program that prints the docstring of this function when it runs.
'''

def square(n):
    '''the docstring for this program is that it will multiply the value by itself 
to give us the value of which would be the square of the one we entered
'''
    return n*n
print(square.__doc__) 

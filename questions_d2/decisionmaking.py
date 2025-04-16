'''
q1)Check if a number is positive, negative, or zero:
Write a program that takes an integer input from the
user and prints whether the number is positive, negative, or zero.'''

def check_p(x):
    if x==0:
        print('zero')
    elif x>0:
        print('positive')
    else:
        print('negative')        

'''
q2)Find the largest of three numbers: 
Write a program to take three numbers 
as input and print the largest number using if-else statements.'''  

def greatest_ofthree(a,b,c):
    if a > b and a > c:
        print('A is greatest: '+ str(a))
    elif b > a and b > c:
        print('B is greatest: '+str(b))
    else:
        print('c is greatest: '+str(c))    

'''
q3)Check if a year is a leap year: 
Write a program that takes a year as input and checks if it is a leap year. '''        

def check_leapyear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print('its a leap year') 
    else:
        print('its not a leap year')  
'''
q4)Check if a number is even or odd: 
Write a program that checks if a given number is even or odd.''' 
def odd_eve(number):
    if number%2==0:
        print('its even')
    else:
        print('its odd')  
x=24029
'''
q5)Grade categorization: 
Write a program that takes a score (0-100) as input and 
prints the grade as per the following criteria:

90 and above: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Below 60: "F"
'''       
def report_card(score):
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >=70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')

'''
q6)Check if a number is divisible by both 3 and 5: 
Write a program that checks if a given number is 
divisible by both 3 and 5. If so, print "Divisible by both". 
Otherwise, print "Not divisible by both".
'''
def dv(x):
    if x%3==0 and x%5==0:
        print('its div by both')
    else:
        print('its not div by both')    
'''
q7)Find the smallest of three numbers: 
Write a program that takes three integers 
as input and prints the smallest one using if-else statements.
'''
def smallest(a,b,c):
    if a < b and a < c:
        print('A is smallest: '+ str(a))
    elif b < a and b < c:
        print('B is smallest: '+str(b))
    else:
        print('c is smallest: '+str(c))

'''
Check if a string contains only digits: 
Write a program that checks if a given string 
contains only digits using an if-else condition.'''
def digimon(a):

    def check_digits(x):
        for char in x:
            if char < '0' or char > '9':
            
                return False
        return True
  
    if check_digits(a):
        print('good')
    else:
        print('bad')

'''
Check if a number is prime: 
Write a program that checks if a 
given number is prime. A prime number 
is only divisible by 1 and itself.'''
def check_prime(x):
    def is_prime(x):
        if x<=1:
            return False
    
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True    

    if is_prime(4):
        print('yeahh')
    else:
        print('nope')    
'''
Check if a number is a perfect square: 
Write a program that checks if a given number is 
a perfect square.'''
def check_perfect(x):
    def check_square(n):
        if n<0:
            return False
        root=int(n**0.5)
        return root*root ==n    
    if check_square(x):
        print('perfect square')
    else:
        print('not perfect square')          
       
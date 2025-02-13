##
#CUSTOM MODULE   
##

import custommodule as cm

cm.Mymodule('its working!')

##
#USING MORE MODULES
##

import math
def sqrt():
    a=int(input('Enter the number: '))
    sqrt_values=math.sqrt(a)
    print('The square root of the number entered is: ',sqrt_values)
def fact():
  
    a=int(input('Enter the number: '))
    factorials=math.factorial(a)
    print('The factorial of the given number is: ',factorials)    

def lcm():
    a=list(map(int,input('Enter the number: ').split()))
    letsee=math.lcm(*a)
    print('LCM of the entered numbers is: ',letsee)    


import os

def os_fun():
    current_directory=os.getcwd()
    list_dir=os.listdir()
    print('The current directory is: ',current_directory)
    print('The list of directories are: ',list_dir)

import random as rd
def rolling():
    return rd.randint(1,6)

print("Do you want to roll a dice?")



#print('do you want to roll again?')
#choice=input().lower()
while True:
    choice=input().lower()
    if choice=='y':
        y=rolling()
        print('the result is: ',y)
        print('do you want to roll again?')
        result=input().lower()

        if result!='y':
            print('exiting the game....')
            break
        else:
            j=rolling()
            print('the rolled result is:',j)
            print('do you want to roll again?')
            continue
            
    else:
        print('exiting the game....')
        break

    
    
   
    


    



def randomness():
    names=['abhishek','saurav','Manuraj','nishant','shukla','vibhu']
    rd.shuffle(names)
    print(names)
    rand=rd.choice(names)
    print(rand)

import datetime as dt

def date_time():
    print('Current date and time is: ',dt.datetime.now())
    print(dt.date.today())

##
#USING PACKAGES (CUSTOM ONE) 
##
from mypackage.module1 import greet

greet()
#result=mypackage.greet()

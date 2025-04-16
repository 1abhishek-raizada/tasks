'''program to print items in a list'''

def print_list(): 
    def find_list(list):
        for x in list:
            print(x)
    li=(1,23,4,'Abhishek')        
    find_list(li)        
'''
Print all prime numbers from 1 to N: 
Write a program that prints all prime 
numbers from 1 to N using a for loop.'''

def print_prime(n):
    def is_prime(x):
        if x<=1:
            return False
    
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True
    for j in range(n):
        if is_prime(j):
            print(j)

'''
Print a multiplication table: 
Write a program that prints the multiplication 
table for a number provided by the user (1-10).'''
def print_table(x):
    for i in range(1,11):
        print(str(x) + "x"+ str(i) +'=' + str(x*i))
'''
Sum of all even numbers between 1 and 100: 
Write a program that calculates the sum of 
all even numbers between 1 and 100 using a for loop.
'''
def print_sume():
    result=0
    for x in range(1,101):
        if x%2==0:
            result+=x
    return result        
'''
count the number of vowels in a string: 
Write a program that takes a string as input 
and counts the number of vowels (a, e, i, o, u) in it using a for loop.'''
def print_vowelcount(str):
    str1='aeiouAEIOU'
    count=0
    for x in str:
        if x in str1:
            count+=1
    print(count)        
'''
Find the factorial of a number: 
Write a program that computes the 
factorial of a number using a for loop.
'''
def fact(x):
    result=1
    
    for i in range(1,x+1):
        result*=i
    print(result)    
'''write a program to print pyramid '''

def pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(1,2*i):
            print('*',end='')
        print()        
 

'''
write program to find sum of n numbers'''

def sum(x):
    result=0
    for i in range(x+1):
        result+=i
    print(result)

'''remove vowels from a string'''
def removeVowels(input_string):
    vowels='aeiouAEIOU'
    result=''
    for char in input_string:
      if char not in vowels:

        result+=char
    return result
print(removeVowels('abhihsek raizada'))

'''
python program to find number of odd and even numbers in a given range
'''
def find_count(a,b):

    count=0
    count1=0
    for x in range(a,b+1):
        if x%2==0:
            count+=1
        else:
            count1+=1
    print(count,count1)            


          



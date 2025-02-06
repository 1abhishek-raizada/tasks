#q1 access elements from a tuple
#write a program that creates a tuple and prints specifics elements using indexing
def q1():
    t1=(1,2,3,4,5)
    for x in t1:
        print(x)
#q2 concatenate and repeat tuples
# write a program that concatenates two tuples and repeats a tuple multiple times.
def q2():
    t1=(1,2,3,4)
    t2=('apples','oranges','bananas')
    t3=t1+t2
    print(t3)        

#find the index of an element in a tuple
# write a program that takes user input to search for an element in a tuple and returns its index
def q3():
    x=input('enter the elements of tuples: ').split()
    t1=tuple(x)
    print(t1)
    target=input('enter the target value: ')
    if target in t1:
        print(t1.index(target)) 
#convert a tuple to a list and modify it
#write a program that converts a tuple into a list, modifies an element and converts it back to 
# a tuple

def q4():
    t1=(1,2,3,4)
    print(t1)
    l1=list(t1)
    l1.append('abhishek')
    print(l1)
    t1=tuple(l1)
    print(t1)
#tuple unpacking
# write a program that unpacks a tuple into individual variables and prints them

def q5():
    t1=('green','apple','orange')
    (red,bright,yellow)=t1
    print(red)
    print(bright)
    print(yellow)
# sets questions now
# q1 create and display a set
# write a program that creates a set,adds elements, and prints the final set.
def set_q1():
    s1={1,2,3,4}
    s1.add('raizada')
    print(s1) 
#q2 find union,intersection and differences of two sets
#write a program that performs and prints union, intersection and difference between two sets.
def set_q2():
    s1={1,2,3}
    s2={1,5,6}
    s3=s1.union(s2)
    print(s3)
    s4=s1.intersection(s2)
    print(s4)
    s5=s1.difference(s2)
    print(s5)
   

#q3 check if an element exists in a set
#write a program that asks the user for a number and checks if it is present in a predefined set.

def set_q3():
    s1={1,2,3,4,5}
    x=int(input('enter a number from 1 to 5: '))
    if x in s1:
        print('it is there in set')
    else:
        print('enter a valid number')    
#q4 remove duplicates from a list using a set

def set_q4():
    list=[1,2,3,4,4,5,5,67,8]
    s1=set(list)
    print(s1)
#dictionary questions
# q1 create a dictionary and access elements
#write a program that updates an existing key-value pair in a dictionary and deletes a specific key.
def dict_q1():
    dict1={1:'apples',2:'oranges'}
    dict1.update({1:'cherry'})
    print(dict1)
    dict1.pop(2)
    print(dict1)
#q2 iterate through nested dictionary and print the items
def dict_q2():
    dogs={1:{1:'pitbull',2:'saint bernard'},2:{1:"golden",2:"brown",3:"black"}}
    print(dogs[2][3])
    for x,obj in dogs.items():
        print(x)
        for y in obj:
            print(y ,':',obj[y])    
   
#questions for list
'''
Write a program that creates a list of at least 
five elements and demonstrates the use of the 
following operations: appending an element, 
inserting an element at a specified index, 
removing an element by its value, and using the pop method.
'''
def q1():
    fruits=[1,2,3,4,5,5,6,7]
    fruits.append(8)
    print(fruits)
    fruits.insert(0,0)
    print(fruits)
    fruits.remove(5)
    print(fruits)
    fruits.pop()
    print(fruits)

'''
Write a program that takes a list of 
numbers and prints the list in reverse 
order using two different methods: one 
by modifying the original list in place, 
and one by creating a new reversed list using slicing.
'''
def reverse_list():
    list1=[1,2,3,4,5,6]
    list1.reverse()
    print(list1)
    list2=[]
    for x in list1[::-1]:
        list2.append(x)
    print(list2)
'''
Write a program that accepts a list of strings 
and a target string from the user. Check if the 
target string is present in the list. If it is, 
print its index; if not, display an appropriate message.
'''
def q3():
    x=input('enter the strings: ')
    list=x.split()
    y=input('enter the target string: ')
    for j in list:
        if y==j:
            print(list.index(j))
            break
        elif y not in list:    
            print('item not found')   
'''
Write a program that finds and prints 
the maximum and minimum values from a 
list of numbers without using the built-in 
`max()` or `min()` functions.
'''
def min_max():
    list=[12,32,123,21,1,211,3,123123,0,-20]
    max=0
    min=list[0]
    for x in list:
        if max<x:
            max=x
        if min>x:
            min=x    
     
    print(max)   
    print(min)    

#some functions use 
# simple function with arguments
def sum(x,y):
    print(x+y)
sum(3,5)    

#using keyword argument
def fun(c1,c2,c3):
    print('the hero is: ' + c3)
fun(c1='goku',c2='saitama',c3='eren') 
#using lambda
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))   


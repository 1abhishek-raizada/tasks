def fib_series(x):
    result=[]
    
    a=0
    b=1
    
    while a<=x:
        result.append(a)
        a=b
        b=a+b
    return result
fs=fib_series(100)
print(fs)   
#positional argument
def person(name,age): 
    print(name,end='')
    print(age)
person(age=22,name='abhishek ') #this is an example of keyword argument even if the position
                               #is wrong we will get the right answer
person('abhishek ',22)          #this is an example of positional argument       
#default argument:
def person(name,age=20):
    print(name,end='')
    print(age)
person('raizada ')       

#variable length arguments
def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
    print(c)
sum(1,2,3,4,4,5,6,7,7,8)    

#keyword variable length arguments or **kwargs
def persons(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)    #i is key and j is value
persons('abhishek',age=21,city='chandigarh',mob=123123111)       

#variable with local scope
def fun():
    x=11
    print(x)
fun()    

#variable with global scope
c=10
def fnc():
    print(c)
print(c)  

#global keyword
l=21
def glo():
    
    l=10
    j=globals()['l'] 
    print(j)
glo()    
print(l)
#use of globals() function
ga=23
def glob():
    ga=15
    print('local',ga)
    y=globals()['ga']
    print('global ga:',y)
    #globals()['ga']=20
glob()

#passing a list to a function 
def count_oddev(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1       
    return even,odd
lst=[21,123,41,4,1,12,2,2]
even,odd=count_oddev(lst)
print('even:  {}  and odd:  {}  '.format(even,odd))
  
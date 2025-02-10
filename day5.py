
from itertools import chain

#flatten a nested list

def list_comprehension():
    a=[[1,2],[3,4],[5,6]]

#here first loop runs the outer list and then the inner by the next one
#this method only works for a nested list with single level
    checked= [x for sublist in a for x in sublist] #list comprehension
   #print(checked)
# itertools also works with single level nested lists
def iter_tools():
    a=[[12,13,13,[12,231]],[123,2,3,4,5],[1,[1,23]]]
    res=list(chain(*a))
    print(res)
#iter_tools()    

# using recursion
def recursively(a):
   
    res=[]
    for x in a:
        if isinstance(x,list):
            res.extend(recursively(x))
        else:
            res.append(x)
    return res  
a=[1,[2,3],4,[5,[6,7,8]]]
#print(recursively(a))          

#using stack
#even stack can be used for deep nested lists
def using_stack(a):
    result=[]
    stack=[a]
    while stack:
        current=stack.pop()
        if isinstance(current,list):
            stack.extend(reversed(current))
        else:
            result.append(current)
    return result
#print(using_stack([1,2,3,4,[23,4,[321]]]))

#
# OOPs concepts
# #

#class
class Computer:
    def config(self):
        print('i5, 16gb ram,1TB')

comp1=Computer() 
comp2=Computer()
Computer.config(comp1)
Computer.config(comp2)
comp1.config()
#__init__ method

class Computer1:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        
    def config(self):
        print('configuration is: ',self.cpu,self.ram)

com1=Computer1('i7','16gb')
com1.config()
           
#types of variables
class Car:
    wheels=4              #this one is class variable
    def __init__(self):
        self.mil=10       #this one is instance variable
        self.com='bmw'
c1=Car()
c1.mil=20
c1.com='audi'
print(c1.com,c1.mil,c1.wheels)                  

#types of methods

class Students:
    school='aps'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @classmethod
    def info(cls):
        return cls.school
    def avg(self):
        return (self.m1+self.m2+self.m3)/3    #this right here is an instance method
    @staticmethod
    def cll():
        print('this is a static method')
s1=Students(12,14,16)
s2=Students(21,32,12)
s3=Students(12,5,6)
print(s1.avg())
print(s2.avg())
print(s3.avg())
print(Students.info())
Students.cll()
##
# INHERITANCE
# #

class A:                                    #parent class
    def feature1(self):
        print('feature 1 is working.....')

    def feature2(self):
        print('feature 2 is working.....')
class B:                                 #child class
    def feature3(self):
        print('feature 3 is working.....')

    def feature4(self):
        print('feature 4 is working.....')   
a=B()
a.feature3()   
#a.feature1()    


class C(A,B):
    def __init__(self):
        print('this is multiple inheritance')

    def feature5(self):
        print('this feature is also working....')

b=C()
b.feature1()
b.feature5()        

##
# POLYMORPHISM
##
class Pycharm:
    def features(self):
        print('its good')
        print('i just like this')

class vscode:
    def features(self):
        print('not so good')
        print('i just dont like it')

class laptop:
    def code(self,ide):
        ide.features()

cde=vscode()
dde=Pycharm()
lap1=laptop()
lap1.code(dde)       

#operator overloading
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other,vector):
            return vector(self.x+other.x,self.y+other.y)
        return NotImplemented
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1=vector(3,5)
v2=vector(2,4)
result=v1+v2
print(result)     

#class overloading
class cat:
    def move(self):
        print('the cat is moving')
class dog:
    def move(self):
        print('the dog is moving')
cat1=cat()
dog1=dog()   
cat1.move()
dog1.move()

##
#ABSTRACTION 
##
from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def engine(self):
        pass

class Bmw(Car):
    def engine(self):
        print('this is BMW M4')
car1=Bmw()
car1.engine()        

##
# ENCAPSULATION
##

#public data members
class stu:
    _rollno=None                    #protected data members
    _branch=None                    #protected data members
    __year=None                     #private data member
    def __init__(self,name,age,roll,branch,year):
        self.name=name
        self.age=age                 #these are public data members
        self._rollno=roll
        self._branch=branch
        self.__year=year
    def display(self):
        print('age is: ',self.age)
    def _displayrollandbranch(self):    #for protected 
        print('roll:',self._rollno)
        print('branch:',self._branch)   

    def __displayyear(self):            #for private
        print('year is:',self.__year)     

    def accessPrivate(self):
        self.__displayyear()


student1=stu('abhishek',22,1,'cse',2024)
student1.display()
student1._displayrollandbranch()
student1.accessPrivate()



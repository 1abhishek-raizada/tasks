#variables in python
import sys
print(sys.version)
x=19
y='abhishek raizada'
#print(x,y)
class myfunc():
    print('oops')
    
add=myfunc()
#print(add)    

#different datatypes
a=1
b='abhishek'
c='c'
d=True
e=[1,2,3,4,'sine']
f=(1,2,3,4,5,6)
g={11,22,11,22,33}
h={1:'abhishek',2:'Raizada',3:[1,2,3],4:32,4:21}
print(a,b,c,d,e,f,g,h)
ac=dict(name='abhishek',age=21)

print(ac)
jh=ac.items()
print(jh)
print(ac.keys())
print(ac.values())
ac['place']='india'
print(ac)
def removeVowels(input_string):
    vowels='aeiouAEIOU'
    result=''
    for char in input_string:
      if char not in vowels:

        result+=char
    return result    
str="abhishek"
xd=removeVowels(str)
print(xd)
dogs={1:{1:'pitbull',2:'saint bernard'},2:{1:"golden",2:"brown",3:"black"}}
print(dogs[2][3])
for x,obj in dogs.items():
   print(x)
   for y in obj:
      print(y ,':',obj[y])
   
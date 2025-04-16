a=8
b=8
c=a+b
print(c)
#lists
list=[1,2,3,4,5,6,7,'abhishek']
print(list[:5])
#x=int(input('tell your number: '))
if 'abhishekk' in list:
    print('yeahh')
else:
    print('nooo')    
    
#
# tuples
# #
#x=input("enter the fruit: ")
fruits=('mango','sitaphal','apple','orange','strawberry')
vegetables=('turnip','spinach','potato')
fregies=fruits+vegetables
#print(fregies)
#hello
##
# SETS#
tset={23,1,2,3,4,5,5,64,32,132}
print(tset)
for i in tset:
    print(i)
tset.add(21)   
dry={'eminem','jayz'}
tset.update(dry)
print(tset) 
tset.remove('eminem')
print(tset)
x=tset.pop()
print(tset)
print(x)

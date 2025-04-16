s='hello'    #normal string
print(s[1])  #this is for printing the particular character of string
print(len(s))
print(s + " there bro")

#can use str() method to convert any input to string type
pi=3.174
newpi='value of pi '  + str(pi)
print(newpi)

st='aa bb cc dd ee ff'
print(st.split(' '))
j=s.encode()
print(j)
#to modify a string we can use slicing
jk='sh' + s[1:]
print(jk)
#p1
def donuts(count):
  # +++your code here+++
  if count < 10:
    return count
  else:
    return 'many'
x=int(input('enter the number: '))
y=donuts(x)
print('the number of donuts: '+ str(y))  
#p2
def both_ends(s):
  # +++your code here+++
  if len(s)<2:
    return 0
  else:
    a=s[:2] 
    b=s[-2:]
    return a+b
str="abhishek"
print(both_ends(str)) 
#p3
def fix_start(s):
  # +++your code here+++
  a=s[:1]
  b=s[1:]
  c=a+b.replace(a,'*')
  return c
str1="sheshnag"
print(fix_start(str1))
  
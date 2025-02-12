##
#FILE READING 
##
def readonly():
    file=open('readfile.txt','r')
    content=file.read()
    print(content)
    file.close()

##
#File reading in binary mode   
##
def readonlyb():
    file=open('readfile.txt','rb')
    content=file.read()
    print(content)
    file.close()

##
#writing a file 
##
def write_newfile():
    file=open('newfile.txt','w')
    file.write('hoi what the hell!')
    file.close()

# appending data onto file

def append_file():
    file=open('newfile.txt','a')
    file.write('sorry for the above statement')
    file.close()

'''
with open('newfile.txt','r') as file:
    content=file.read()
    print(content)    
'''
#working with CSV files

import csv

filename1='post_edu.csv'
fields=[]
rows=[]

with open(filename1,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
    print('total number of rows: %d'%(csvreader.line_num))  
print('field names are:' + ','.join(field for field in fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print('%10s' %col,end='')
    print('\n')    

##
#working with pandas 
##    
import pandas as pd

df=pd.read_csv('post_edu.csv')


print(df.head())
print(df.head(2))
print(df)
print(df.info())
print(df.describe())

name=['abhishek','abhay','arhaan','deven']
age=[22,22,23,24]
deg=['cse','arts','civil','electronics']
dict={'name':name,'age':age,'deg':deg}
print(dict)
jk=pd.DataFrame(dict)
print(jk)
col_name=jk['age']
print('mode is: ',col_name.mean())
print('median is: ',col_name.median())
print(col_name.mode())
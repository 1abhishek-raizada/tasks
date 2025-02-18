##
#USING NUMPY 
##


import numpy as np

arr1=np.array([1,2,3,4,5,6])            #list as an input
print(arr1)         
arr2=np.array((1,2,3,4,4))              #tuple as an input
print(arr2)
arr3=np.array(23)                       #0-Dimension array
print(arr3)

print(arr1.ndim)
print(np.array([[1,2,3],[1,2,3]]).ndim)

#accessing array elements
print('Index of the element at 0 is:',arr1[0])
print('sum of elements at index 0 and 2 is:',arr1[0]+arr1[2])
#getting shape
print(arr1.shape)
#accessing different elements
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a.shape)
print(a)
print(a[1,5])                         #will output the fifth element in first row = 13
#getting a specific row
print(a[0,:])
#getting a specific column
print(a[:,2])

#initializing different types of arrays

#all zeros matrix
b=np.zeros((2,3))
print(b)

#all ones matrix
c=np.ones((2,4))
print(c)

ran=np.random.rand(2,4)
print(ran)      

#working with matrix

output=np.ones((5,5))
print(output)

z=np.zeros((3,3))
print(z)
z[1,1]=9
print(z)
output[1:-1,1:-1]=z
print(output)

#find the determinant

det=np.identity(3)
detval=np.linalg.det(det)
print(detval)

#STATISTICS

stats=np.array([1,2,3,4,5,5,6,6,7,8,8,9,9,10])
print('Mean value of the given array is:',stats.mean())                 #mean
print('Max value of the given array is:',stats.max())                   #max
print('Min value of the given array is:',stats.min())                   #min
print('Sum of all the values of the given array is:',stats.sum())       #sum

#vertically stacking arrays

a1=np.array([2,3,4])
a2=np.array([5,6,7])
stacked=np.vstack((a1,a2))
print(stacked)

#horizontally stacking arrays
b1=np.array([1,2,3])
b2=np.array([4,5,6])
hstacked=np.hstack((b1,b2))
print(hstacked)


##
#working with pandas 
##    
import pandas as pd

df=pd.read_csv('tasks/post_edu.csv')


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
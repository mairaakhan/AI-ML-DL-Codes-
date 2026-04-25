#U = Unicode string
#6 = Maximum of 6 characters per string

import numpy as np

arr = np.array(['apple' , 'banana' , 'mango'])
print(arr.dtype)

#dtype tells you the data type of a NumPy array.
#It does not change anything.
#Think of it as a property or label of the array.

#dtype='S' means store the values as bytes (string type) instead of integers.So NumPy converts each number into a byte string.
#b'1' → byte string (not a normal integer anymore) and max length is 1 character
arr = np.array([1,2,3,4,5,6],dtype = 'S')
print(arr)
print(arr.dtype)

#i = integer
#4 = 4 bytes (32 bits)

arr = np.array([1,2,3,4,5] , dtype = 'i4')
print(arr)
print(arr.dtype)

#
arr = np.array([1,2,3,4,5] , dtype = 'f4')
print(arr)
print(arr.dtype)

arr = np.array([1,2,3,4] , dtype = 'b')
print(arr)
print(arr.dtype)

arr = np.array(['a',2,3,4] , dtype = 'U')
print(arr)
print(arr.dtype)

# Convert the float array to integer type
arr = np.array([1.1, 2.1, 3.1, 4.2] , dtype = 'i')
print(arr)
print(arr.dtype)

#astype() creates a new array with a different data type.
#It converts the elements to the new type.
#It returns a copy, leaving the original array unchanged.

#astype() does not modify the original array.
#It returns a new copy with the new data type.
arr = np.array([1.1, 2.1, 3.1, 4.2])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#astype('bool') converts numbers to True or False:
#Any non-zero number → True
arr = np.array([1.1, 2.1, 3.1, 4.2, 0])
newarr = arr.astype('bool')
print(newarr)
print(newarr.dtype)

#A copy is a completely new array in memory.
#Changes to the copy do not affect the original array

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 43
print(arr)
print(x)


#A view is a new array object that shares the same data with the original.
#Changes in the view affect the original array.
#Views are memory-efficient because they don’t copy the data.

arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 43
print(arr)
print(x)


#A view is a new array object that shares the same data with the original.
#Changes in the view affect the original array.
#Views are memory-efficient because they don’t copy the data.
#here we make changes in view array not copy

arr = np.array([1,2,3,4,5])
x = arr.view()
x[0] = 43
print(arr)
print(x)


#base tells you if an array is a copy or a view.
#if its own then give array
#if it doesn't own then it gives none

arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#shape
#tells rows and column
#(rows, column)
arr = np.array([[1,2,3,4,5] , [1,2,3,4,5]])
print(arr.shape)


#This creates an array with at least 5 dimensions.
#Your 1D list [1,2,3,4,8] is “wrapped” in extra dimensions to make it 5D.
#The brackets show 5 levels of nesting → 5D array
#.shape shows the size in each dimension.
arr = np.array([1,2,3,4,8] , ndmin = 5)
print(arr)
print(arr.shape)
print(arr[0,0,0,0,1])

#reshape changes the shape of the array without changing the data.
#You are asking for 4 rows and 3 columns.
#Original array has 12 elements → fits perfectly into 4×3.

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3) ## Reshape into 4 rows and 3 columns
print(newarr)

#1
#(outer array, inner array, no of elements)
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)

#2
#(outer array, inner array, no of elements)
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,2,3)
print(newarr)

#check if return array is a  copy or view?
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)

#-1 is a placeholder.
#NumPy automatically calculates the correct size for that dimension based on the total number of elements.
#we can not pass -1 to more than one dimension means arr.reshape(-1, -1, -1)  # ❌ Error

arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4,-1))

#converts array into 1-D
arr = np.array([[1,2,3,4] , [5,6,7,8]])
newarr = arr.reshape(-1)
print(newarr)

arr = np.array([1,2,3,4])
for i in arr:
    print(i)

arr = np.array([[1,2,3,4] , [5,6,7,8]])
for i in arr:
    for j in i:
        print(j)

arr = np.array([[1,2,3,4] , [5,6,7,8]])
for i in arr:
    for j in i:
        print(i[2])
        break

arr = np.array([[[1,2,3,4] , [5,6,7,8]] , [[5,6,7,8] , [5,6,7,8]]])
for i in arr:
    print(i)
    for j in i:
        print(j)
        for z in j:
            print(z)

#dont need to use nested loop if we use this
#np.nditer, which is a very powerful way to iterate over all elements of a NumPy array
arr = np.array([[[1,2,3,4] , [5,6,7,8]] , [[5,6,7,8] , [5,6,7,8]]])
for i in np.nditer(arr):
    print(i)




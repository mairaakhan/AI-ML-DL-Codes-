#Numpy
#use a list to create numpy array
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr)

#printing np version
print('version:',np.__version__)

#printing type of np
print('Type:', type(arr))


#use a tuple to create numpy array
import numpy as np
arr = np.array((1,2,3,4,5,6,7))
print(arr)

#dimension
import numpy as np

# =========================
# 0-D ARRAY
# =========================
# Create a 0-D array with value 42

print("0-D ARRAY")
arr = np.array(42)
print(arr)


# =========================
# 2-D ARRAY AS LIST
# =========================
# An array that has 1-D arrays as its elements is called a 2-D array

print("\n2-D ARRAY AS LIST\n")
arr = np.array([[1, 2, 4],[3, 4, 4]])
print(arr)
# arr = np.array([[1,2,4], [3,4]])  # Dimension error example

# =========================
# 2-D ARRAY AS TUPLE
# =========================

print("\n2-D ARRAY AS TUPLE\n")
arr = np.array(([1, 2],[3, 4]))
print(arr)


# =========================
# 3-D ARRAY
# =========================
# An array that has 2-D arrays as its elements is called a 3-D array

print("\n3-D ARRAY\n")
arr = np.array([[[1, 2, 4],[3, 4, 4]] , [[8, 9, 10],[12, 13, 24]]])
print(arr)

#check how many dimension a array have
a = np.array(42)
b = np.array([1,2,3,4,5,6,7])
c = np.array([[1,2,4], [3,4,4]])
d = np.array([[[1,2,4], [3,4,4]] , [[8,9,10], [12,13,24]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#create an array with 5 dimensions and verify that its has 5 dimensions
arr = np.array([1,2,3,4,5] , ndmin = 5)
print(arr)
print('Number of dimensions:' , arr.ndim)

#[row, index/element] ---- 2-D array
arr = np.array([[1,2,4], [3,4,10]])
print(arr[0,2])
print(arr[0,-2])
print(arr[1,2])

#[row, array, element] ---- 3-D array
arr = np.array([[[1,2,4], [3,4,4]] , [[8,9,10], [12,13,24]]])
print(arr[0,1,2])
print(arr[0,-1,2])
print(arr[1,1,1])



#NumPy array slicing
#[start : end]
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:])
print(arr[:])
print(arr[3:5])
print(arr[3:-2])

print()

#[start : end : steps]
print(arr[1 : 5 : 3])
print(arr[ : : 2])

print()

#[row, array:element ]
arr1 = np.array([[1,2,4], [3,4,8]])
print(arr1[1,1:2])

print()

#[ array:element , row]
print(arr1[1:2,1])

print()

print(arr1[ 0: , 1:] )

arr = np.array([0,1,2,3,4])
print(arr.dtype)




import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)


import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


import numpy as np
arr = np.arange(1, 21)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]
print("Even numbers:", even)
print("Odd numbers:", odd)


import numpy as np
arr = np.arange(1, 13)
print("2 x 6 Matrix:")
print(arr.reshape(2, 6))
print("3 x 4 Matrix:")
print(arr.reshape(3, 4))
print("4 x 3 Matrix:")
print(arr.reshape(4, 3))


import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
print("Matrix Addition:")
print(a + b)


import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
result = np.matmul(a, b)
print("Matrix Multiplication:")
print(result)


import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print("Original Matrix:")
print(a)
print("Transpose:")
print(a.T)


import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
print("First Row:", a[0])
print("Last Column:", a[:, -1])
print("Diagonal Elements:", np.diag(a))
print("Second and Third Rows:")
print(a[1:3])


import numpy as np
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
print("Sum of each row:", np.sum(a, axis=1))
print("Sum of each column:", np.sum(a, axis=0))


import numpy as np
arr = np.arange(1, 21)
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])
print("Reverse order:", arr[::-1])


import numpy as np
arr = np.array([10, 25, 55, 70, 30, 80, 45, 90, 20, 60])
arr[arr > 50] = 0
print("Array after replacement:", arr)


import numpy as np
arr = np.array([50, 20, 80, 10, 40, 90, 30])
print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])


import numpy as np
arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 10])
print("Unique elements:", np.unique(arr))


import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print("Horizontal Concatenation:")
print(np.hstack((a, b)))
print("Vertical Concatenation:")
print(np.vstack((a, b)))


import numpy as np
marks = np.array([75, 82, 68, 90, 55, 78, 88, 95, 72, 85])
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


import numpy as np
marks = np.array([45, 67, 89, 55, 72, 90, 34, 78, 81, 60,
                  92, 50, 76, 88, 65, 70, 95, 40, 58, 83])
average = np.mean(marks)
print("Class Average:", average)
print("Marks above average:", marks[marks > average])


import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:")
print(arr)
print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:")
print(np.sum(arr, axis=(1, 2)))
print("Sum along rows:")
print(np.sum(arr, axis=2))
print("Sum along columns:")
print(np.sum(arr, axis=1))


import numpy as np
arr = np.random.randint(1, 101, size=(2, 3, 4))
print("Original Array:")
print(arr)
arr[arr > 50] = 0
print("After replacing values greater than 50:")
print(arr)


import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
print("Array:")
print(arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D Array:")
print(arr)
flat = arr.flatten()
print("Flattened Array:")
print(flat)


import numpy as np
arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()
print("3D Array:")
print(arr)
print("Flattened Array:")
print(flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
print("Original 3D Array:")
print(arr)
print("Elements greater than 50:")
print(flat[flat > 50])
print("Even numbers:")
print(flat[flat % 2 == 0])
average = np.mean(flat)
print("Average:", average)
print("Elements less than average:")
print(flat[flat < average])
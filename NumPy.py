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
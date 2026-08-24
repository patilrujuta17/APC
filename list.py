# Create a list of five fruits and display the list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("List of fruits:")
print(fruits)

# Create a list of five integers
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])

# Create a list of colors
colors = ["Red", "Blue", "Green", "Yellow", "Orange"]
colors[2] = "Purple"
print("List:",colors)

# Create a list of numbers
numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(0, 5)
numbers.insert(3, 25)
print("Updated list:", numbers)

# Create a list of student names
students = ["Riya", "Amit", "Sneha", "Rahul", "Neha"]
students.pop(0)
students.pop()
students.remove("Sneha")
print("Remaining students:", students)

# find the smallest and the largest in the list
numbers = [25, 10, 45, 5, 30]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest number:", largest)
print("Smallest number:", smallest)

# Accept 10 numbers from the user and calculate sum and average
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
total = sum(numbers)
average = total / 10
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)

# Store 15 integers in a list and count how many numbers are even and odd
numbers = [10, 15, 22, 7, 18, 25, 30, 11, 14, 9, 20, 33, 16, 5, 40]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

# Create a list of cities and ask the user to enter a city name and check whether it exist in the list
cities = ["Pune", "Mumbai", "Delhi", "Kolhapur", "Nashik"]
city = input("Enter a city name: ")
if city in cities:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")

# Create a list of 10 numbers
numbers = [10, 20, 30, 40, 50]
reversed_list = numbers[::-1]
print("Original list:", numbers)
print("Reversed list:", reversed_list)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])

# accept  10 numbers and sort them in ascending and decending order
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print("Elements at even index positions:", numbers[::2])
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
print("Ascending order:", ascending)
print("Descending order:", descending)

# Create a list with duplicate values and display only unique values
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Original list:", numbers)
print("Unique elements:", unique)
numbers = [10, 25, 45, 30, 50, 20]
unique = list(set(numbers))
unique.sort(reverse=True)
second_largest = unique[1]
print("Second largest element:", second_largest)

# Create a nested list storing all student details
students = [
    ["Riya", 101, 85],
    ["Amit", 102, 90],
    ["Sneha", 103, 78],
    ["Rahul", 104, 88]
]
for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()

# Create two 3 × 3 matrices and perform matrix addition
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print("Matrix Addition:")
for row in result:
    print(row)

# Create an empty shopping cart and perform operations
cart = []
cart.append("Apple")
cart.append("Milk")
cart.append("Bread")
cart.append("Rice")
cart.remove("Milk")
item = input("Enter item to search: ")
if item in cart:
    print("Item is available in the cart.")
else:
    print("Item is not available in the cart.")
print("Shopping Cart:", cart)
print("Total items:", len(cart))
students = ["Riya", "Amit", "Sneha", "Rahul", "Neha"]
print("Total students:", len(students))
name = input("Enter student name to check attendance: ")
if name in students:
    print(name, "is present.")
else:
    print(name, "is absent.")
new_student = input("Enter new student name: ")
students.append(new_student)
absent_student = input("Enter absent student name to remove: ")
if absent_student in students:
    students.remove(absent_student)
    print(absent_student, "removed from the list.")
else:
    print(absent_student, "is not in the list.")
print("Updated student list:", students)
print("Total students:", len(students))

# Store names of students present in class and display
students = ["Riya", "Amit", "Sneha", "Rahul", "Neha"]
print("Total students:", len(students))
name = input("Enter student name to search: ")
if name in students:
    print(name, "is present.")
else:
    print(name, "is absent.")
new_student = input("Enter new student name: ")
students.append(new_student)
absent_student = input("Enter absent student name: ")

if absent_student in students:
    students.remove(absent_student)
    print(absent_student, "removed from the list.")
else:
    print(absent_student, "is not present in the list.")

print("Updated student list:", students)
print("Total students:", len(students))

# Create a list of books and perform operations
books = ["Python Basics", "Data Structures", "Computer Networks", "Database Systems"]
new_book = input("Enter a new book: ")
books.append(new_book)
search_book = input("Enter book name to search: ")
if search_book in books:
    print("Book is available.")
else:
    print("Book is not available.")
remove_book = input("Enter book name to remove: ")

if remove_book in books:
    books.remove(remove_book)
    print("Book removed successfully.")
else:
    print("Book not found.")
print("All books:")
for book in books:
    print(book)
print("Total books:", len(books))

# Accept two list and merge them into a single list
list1 = input("Enter elements of first list: ").split()
list2 = input("Enter elements of second list: ").split()
merged_list = list1 + list2
print("Merged list:", merged_list)

# Create two lists and find common elements
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common = []
for num in list1:
    if num in list2:
        common.append(num)
print("Common elements:", common)

# Count the frequency of each element in the list
numbers = [10, 20, 10, 30, 20, 10, 40, 30]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequency of each element:")
for num in frequency:
    print(num, ":", frequency[num])

# Rotate a list
numbers = [10, 20, 30, 40, 50]
left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]
print("Original list:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)

# Remove all the duplicate elemnts while preserving the originall order
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Original list:", numbers)
print("List without duplicates:", unique)

# Store marks of 20 students in the lst and determine
marks = [75, 60, 85, 90, 55, 70, 95, 80, 65, 88,
         72, 50, 92, 78, 68, 84, 45, 76, 82, 58]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
above_average = 0
below_average = 0
for mark in marks:
    if mark > average:
        above_average += 1
    elif mark < average:
        below_average += 1
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above_average)
print("Students below average:", below_average)

# Store salaries of employees and determine
salaries = [25000, 35000, 45000, 55000, 60000,
            28000, 70000, 48000, 52000, 30000]
highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)
above_50000 = 0
below_30000 = 0
for salary in salaries:
    if salary > 50000:
        above_50000 += 1
    if salary < 30000:
        below_30000 += 1
print("Highest salary: ₹", highest)
print("Lowest salary: ₹", lowest)
print("Average salary: ₹", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)

# Store scores of a batsman in 10 matches and calculate
scores = [45, 102, 67, 89, 120, 35, 55, 78, 110, 42]
highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)
centuries = 0
half_centuries = 0
for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)

# Store temperature of 30 days and determine
temperature = [
    30, 32, 29, 31, 35, 33, 28, 30, 34, 36,
    31, 29, 32, 37, 35, 30, 28, 33, 34, 36,
    31, 32, 29, 35, 38, 30, 27, 33, 36, 34
]
hottest = max(temperature)
coldest = min(temperature)
average = sum(temperature) / len(temperature)
above_average = 0
below_average = 0
for temp in temperature:
    if temp > average:
        above_average += 1
    elif temp < average:
        below_average += 1
print("Hottest temperature:", hottest, "°C")
print("Coldest temperature:", coldest, "°C")
print("Average temperature:", average, "°C")
print("Days above average:", above_average)
print("Days below average:", below_average)

# Store patient names and ages usinf list and perform operations
names = ["Riya", "Amit", "Sneha"]
ages = [20, 25, 22]
new_name = input("Enter patient name: ")
new_age = int(input("Enter patient age: "))
names.append(new_name)
ages.append(new_age)
delete_name = input("Enter patient name to delete: ")
if delete_name in names:
    index = names.index(delete_name)
    names.pop(index)
    ages.pop(index)
    print("Patient deleted successfully.")
else:
    print("Patient not found.")
print("Patient details:")
for i in range(len(names)):
    print("Name:", names[i], "Age:", ages[i])
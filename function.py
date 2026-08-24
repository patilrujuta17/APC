# 1.Write a function factorial(n) that accepts an integer and returns its factorial.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(5))

# 2.Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(7))

# 3.Define a function that accepts two numbers and returns the greater number.
def greater_number(a, b):
    if a > b:
        return a
    else:
        return b
print(greater_number(10,20))

# 4.Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    interest = (p * r * t) / 100
    return interest
print(simple_interest(1000, 5, 2))

# 5.Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

# 6.Define a function to calculate the area of a circle using its radius.
import math
def area_of_circle(radius):
    return math.pi * radius * radius
print(area_of_circle(5))

# 7.Write a function that accepts n and returns the sum of the first n natural numbers.
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
print(sum_natural(5))

# 8.Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    return base ** exponent
print(power(2, 3))

# 9.Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def largest_element(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
numbers = [10, 25, 7, 40, 15]
print(largest_element(numbers))

# 10.Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
print(count_vowels("Hello World"))

# 11.Write a function that accepts a string and returns its reverse.
def reverse_string(text):
    return text[::-1]
print(reverse_string("Hello"))

# 12.Create a function that checks whether a given string or number is a palindrome.
def is_palindrome(value):
    value = str(value)
    return value == value[::-1]
print(is_palindrome("madam"))
print(is_palindrome(121))
print(is_palindrome("hello"))

# 13.Write a function that accepts a list of numbers and returns their average.
def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
numbers = [10, 20, 30, 40, 50]
print(average(numbers))

# 14.Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_occurrences(numbers, element):
    count = 0
    for num in numbers:
        if num == element:
            count += 1
    return count
numbers = [1, 2, 3, 2, 4, 2, 5]
print(count_occurrences(numbers, 2))

# 15.Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
numbers = [1, 2, 3, 2, 4, 1, 5]
print(unique_elements(numbers))

# 16.Create a function to find the second-largest number in a list.
def second_largest(numbers):
    largest = second = float('-inf')
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
numbers = [10, 25, 7, 40, 30]
print(second_largest(numbers))

# 17.Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    fib = []
    a, b = 0, 1
    for i in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib
print(fibonacci(7))

# 18.Create a function that accepts marks in five subjects and returns the student's percentage and grade.
def calculate_result(mark1, mark2, mark3, mark4, mark5):
    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade
percentage, grade = calculate_result(85, 90, 78, 88, 92)
print("Percentage:", percentage)
print("Grade:", grade)

# 19.Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7
    return bill
units = 250
print("Electricity Bill:", electricity_bill(units))

# 20.Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
def gross_salary(basic_salary):
    hra = basic_salary * 0.20   # 20% HRA
    da = basic_salary * 0.10    # 10% DA
    gross = basic_salary + hra + da
    return gross
print("Gross Salary:", gross_salary(30000))

# 21.	Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
def total_bill(prices, quantities):
    total = 0
    for price, quantity in zip(prices, quantities):
        total += price * quantity
    discount = total * 0.10
    final_bill = total - discount
    return final_bill
prices = [100, 200, 300]
quantities = [2, 1, 1]
print("Total Bill:", total_bill(prices, quantities))

# 22.	Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
def calculate_values(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total += num
    average = total / len(numbers)
    return minimum, maximum, total, average
numbers = [10, 20, 30, 40, 50]
minimum, maximum, total, average = calculate_values(numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", average)

# 23.Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def calculate_total(marks):
    return sum(marks)
def calculate_percentage(marks):
    total = calculate_total(marks)
    return total / 5
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
def class_average(students):
    total = 0
    for student in students:
        total += calculate_percentage(student["marks"])
    return total / len(students)
def highest_scorer(students):
    highest = students[0]
    for student in students:
        if calculate_total(student["marks"]) > calculate_total(highest["marks"]):
            highest = student
    return highest
def lowest_scorer(students):
    lowest = students[0]
    for student in students:
        if calculate_total(student["marks"]) < calculate_total(lowest["marks"]):
            lowest = student
    return lowest
# Student records
students = [
    {"name": "Riya", "roll": 1, "marks": [85, 90, 78, 88, 92]},
    {"name": "Amit", "roll": 2, "marks": [75, 80, 70, 72, 78]},
    {"name": "Sneha", "roll": 3, "marks": [92, 95, 90, 94, 96]}
]
# Display student details
for student in students:
    total = calculate_total(student["marks"])
    percentage = calculate_percentage(student["marks"])
    grade = calculate_grade(percentage)
    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print()
# Class average
print("Class Average:", class_average(students))
# Highest scorer
highest = highest_scorer(students)
print("Highest Scorer:", highest["name"])
# Lowest scorer
lowest = lowest_scorer(students)
print("Lowest Scorer:", lowest["name"])

# 23.Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def total_marks(marks):
    return sum(marks)
def percentage(marks):
    return total_marks(marks) / 5
def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"
def class_average(students):
    total = 0
    for student in students:
        total += percentage(student["marks"])
    return total / len(students)
def highest_scorer(students):
    highest = students[0]
    for student in students:
        if total_marks(student["marks"]) > total_marks(highest["marks"]):
            highest = student
    return highest
def lowest_scorer(students):
    lowest = students[0]
    for student in students:
        if total_marks(student["marks"]) < total_marks(lowest["marks"]):
            lowest = student
    return lowest
# Student records
students = [
    {"name": "Riya", "roll": 1, "marks": [85, 90, 78, 88, 92]},
    {"name": "Amit", "roll": 2, "marks": [75, 80, 70, 72, 78]},
    {"name": "Sneha", "roll": 3, "marks": [92, 95, 90, 94, 96]}
]
# Display details of each student
for student in students:
    total = total_marks(student["marks"])
    per = percentage(student["marks"])
    g = grade(per)
    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Total:", total)
    print("Percentage:", per)
    print("Grade:", g)
    print("----------------------")
# Class average
print("Class Average:", class_average(students))
# Highest scorer
high = highest_scorer(students)
print("Highest Scorer:", high["name"])
# Lowest scorer
low = lowest_scorer(students)
print("Lowest Scorer:", low["name"])

# 24.Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.
balance = 0
transactions = []
def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))
    print("Amount deposited successfully.")
def withdrawal(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")
def balance_enquiry():
    print("Current Balance:", balance)
def transaction_history():
    print("\nTransaction History:")

    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)
deposit(5000)
balance_enquiry()
withdrawal(1500)
balance_enquiry()
withdrawal(5000)
deposit(2000)
balance_enquiry()
transaction_history()

# 25.	Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.
books = {}
def add_book(book_id, title):
    books[book_id] = {
        "title": title,
        "available": True
    }
    print("Book added successfully.")
def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")
def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned successfully.")
    else:
        print("Book not found.")
def search_book(book_id):
    if book_id in books:
        print("Book ID:", book_id)
        print("Title:", books[book_id]["title"])
        if books[book_id]["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")
    else:
        print("Book not found.")
def display_available_books():
    print("\nAvailable Books:")
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, "-", book["title"])
add_book(101, "Python Programming")
add_book(102, "Data Structures")
add_book(103, "Computer Networks")
issue_book(101)
search_book(101)
return_book(101)
display_available_books()

# 25.	Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.
books = {}
def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}
    print("Book added successfully.")
def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")
def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned successfully.")
    else:
        print("Book not found.")
def search_book(book_id):
    if book_id in books:
        print("Book:", books[book_id]["title"])
        if books[book_id]["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")
    else:
        print("Book not found.")
def display_available_books():
    print("Available Books:")
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, "-", book["title"])
add_book(101, "Python")
add_book(102, "Java")
add_book(103, "Data Structures")
issue_book(101)
search_book(101)
return_book(101)
display_available_books()
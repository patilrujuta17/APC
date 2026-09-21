class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print()
s1 = Student(1, "Riya", [80, 75, 90, 85, 70])
s2 = Student(2, "Amit", [70, 80, 75, 85, 90])
s3 = Student(3, "Priya", [90, 85, 95, 80, 88])
s1.display()
s2.display()
s3.display()



class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
    def calculate(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        gross = self.basic_salary + hra + da
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)
e = Employee(101, "Rahul", 30000)
e.calculate()


class rectangle:
    def __init__(length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate(self):
        area = length*breadth
        perimeter = 2*(length+breadth)
        print("Area of rectangle:", area)
        print("Perimeter of rectangle:", perimeter)
rec = rectangle(5,6)
rec.calculate
    
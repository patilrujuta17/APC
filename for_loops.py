#program to print the natural numbers up to n
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(i, end = " ")
print()

#program to print even numbers up to n
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    if (i%2 == 0):
        print(i, end = " ")
print()

#program to print odd numbers up to n
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    if (i%2 == 1):
        print (i, end = " ")
print()

#program that prints 1 2 8 16       
n = int(input("Enter the value of n: "))
num = 1
for i in range(n):
    print (num, end =" ")
    num = num*2
print()

#program to sum the sequence of 1 + 1/1! + 1/2!
n = int(input("Enter the value of n: "))
fact = 1
sum = 1
for i in range (1, n+1):
    fact = fact*i
    sum = sum + (1/fact)
print("Sum of series: ", sum)
print()

n = int(input("Enter the value of n: "))

# Find the square root if it is a perfect square
square_root = -1
for i in range(1, n + 1):
    if i * i == n:
        square_root = i
        break
if square_root == -1:
    print("The square root is not an integer, so it is not prime.")
else:
    is_prime = True
    if square_root < 2:
        is_prime = False
    else:
        for i in range(2, square_root):
            if square_root % i == 0:
                is_prime = False
                break
    if is_prime:
        print("Prime")
    else:
        print("Non-prime")

#program to produce design
n = int(input("Enter the value of n: "))
for i in range(n):
    for j in range(n):
        print(chr(65+j), end = " ")
    print ()

#program to produce design
n = int(input("Enter the value of n: "))
for i in range(n):
    for j in range(i):
        print(chr(65+j), end = " ")
    print()




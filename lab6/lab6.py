
#Question1a
def print_triangular_numbers(n):
    x = 1
    while x <= n:
        formula = x * (x + 1) / 2
        print x, '\t', formula
        x += 1

#Question1b
def myFactorial(n):
    result = 1
    i = n * (n -1)
    while n >= 1:
        result = result * n
        n = n - 1
    print result


#Question 1c
def checkOddEven():
    for n in range(0,20):
        if(n % 2 == 0):
            print n, "is even"
        else :
            print n, "is odd"
#Question 1d
def printAsterisksV1():
    n = input("Enter asterisks")
    for i in range(n):
        print("*")
#Question 1e
def printAsterisksV2():
    n = input("Enter asterisks")
    i = 0
    while (i<n):
        print("*")
        i+= 1
#Question 1f
def printDiagonally():
    n = input("Enter a string")
    space = " "
    for i in range(len(n)):
        print space*i, n[i]
#Task2
while True:
    choice=input("\n1. Test Exercise 2\n2. Test myFactorial\n3. Test checkOddEven\n4. Test printAsterisksV1\n5. Test printAsterisksV2\n6. Test printDiagonally\n7. Exit\n")
    if (choice==1):
        n = input("Enter a number")

        print_triangular_numbers(n)
    if (choice == 2):
        n = input("Enter a number")
        myFactorial(n)
    if (choice == 3):
        checkOddEven()
    if (choice == 4):
        printAsterisksV1()
    if (choice == 5):
        printAsterisksV2()
    if (choice == 6):
        printDiagonally()
    if (choice == 7):
        break

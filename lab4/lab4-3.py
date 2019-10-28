import math
def computeDistance(x,y,x1,y1):
    return math.sqrt(((x1-x)**2 + (y1-y)**2))
x = int(input("Give x a number: "))
y = int(input("Give y a number "))
x1 = int(input("Give x1 a number "))
y1 = int(input("Give y1 a number "))
print("The distance between 2 points is: ", computeDistance(x,y,x1,y1))
#1
def isSorted():
    list = input("please input a list with comma: ").split(",")
    if list == sorted(list):
        return True
    else:
        return False

#2
def isAnagram():
    letter = input("Write first word here: ")
    letter2 = input("Rearrange the order of the first word here: ")
    if sorted(letter) == sorted(letter2):
        return True
    else:
        return False
#3
def removeDuplicates(u):
    x = []
    for a in u:
        if a not in x:
            x.append(a)
    return x
#4
def sumOfSquare():
    import math
    sum = 0
    list = input("Enter a list here")
    for i in range(len(list)):
        sum += list[i]**2
    return sum
while True:
    demand = int(input(" 1. Test isSorted\n 2. Test isAnagram\n 3. Test removeDuplicate\n 4. Test sumOfSquare\n 5. Exit\n"))
    if demand == 1:
        print(isSorted())
        break
    if demand == 2:
        print (isAnagram())
    if demand == 3:
        print (removeDuplicates())
    if demand == 4:
        print(sumOfSquare())
    if demand == 5:
        break




#Task1
import csv
from csv import DictWriter
files = ['2000_BoysNames', '2000_GirlsNames']

for file in files:
    f = open(file+'.txt', 'r')
    f1 = open(file+'.csv', 'w')
    f1.write('"First Name","Count"\n')
    for i in f:
        j = i.split()
        k = '"' + j[0] + '",' +j[1] + '\n'
        f1.write(k)
    f1.close()
    f.close()
#Task2
def test():
    t = input("Write the name with .csv")
    with open(t) as openNewName:
        check = csv.DictReader (openNewName)
        for testfile in check:
            print('First Name: ' + testfile['First Name'], 'Count: ' + testfile['Count']+ '\n')
test()
def converGas(number,enter):
    if enter ==0:
        MPG2L = round((378.5411784/1.609344*number),2)
        return MPG2L
enter = int(input("Enter 0 to convert MPG to liters/100km or 1 to convert liters/100km to MPG: "))
number = float(input("Enter the number: "))
if enter ==0:
    print (number,"MPG to litters/100km is ",converGas(number,enter))
elif enter ==1:
    print (number,"litters/100km to MPG is ", converGas(number,enter))
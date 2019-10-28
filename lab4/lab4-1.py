def convertTemperature(temperature,enter):
    if enter==0:
        F2C = round(((temperature-32)*5/9),2)
        return F2C
    if enter==1:
        C2F = round(((temperature*9/5)+32),2)
        return C2F
enter = float(input("Enter 0 for Fahrenheit to Celsius, 1 for Celsius to Fahrenheit"))
temperature = int(input("Enter a temperature:"))
if enter == 0:
    print(temperature, "Fahrenheit equal to", convertTemperature(temperature,enter), "Celsius")
elif enter == 1:
    print(temperature, "Celsius equal to", convertTemperature(temperature,enter), "Fahrenheit")


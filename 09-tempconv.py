# Temperature conversion program

temp = float(input("Enter the temperature you wish to convert: "))
unit = input("Enter the unit of the temperature above (F or C): ")

if(unit == 'F' or unit == 'f'):
    temp = round(((temp - 32) * 5 / 9), 1)
    print(f"The temperature in C is: {temp} degrees C")
elif(unit == 'C' or unit == 'c'):
    temp = round(((temp * 9) / 5 + 32), 1)
    print(f"The temperature in F is: {temp} degrees F")
else:
    print(f"{unit} is not a valid unit.")
# input() - a function that prompts the user to enter data
#           && returns the entered data in a string


#
# name = input("What is your name? ")
# # age = input("How old are you? ")
#
# # age = int(age)
# age = int(input("How old are you? "))
# age = age + 1
#
# print(f"Hello, {name}")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years old.")



# # Exercise 1 - Calculate area of a rectangle
#
# length = float(input("What is the length of the rectangle? "))
# width = float(input("What is the width of the rectangle? "))
#
# area = length * width
#
# # super script 2 on mac = Cntrl + Cmd + Space then search for the character
# print(f"The area of the rectangle is {area} units².")



# Exercise 2 - Create a shopping cart program

item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
qty = int(input("How many would you like? "))
total = price * qty

print(f"The total cost of {qty} {item}(s) before tax: ${total}")

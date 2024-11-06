# If statements = do some code only IF something is true
# Else do something else

# age = int(input("Enter your age: "))

# if(age >= 18):
#     print("You can sign up for a credit card")
# elif(age < 0):
#     print("You haven't been born yet")
# # Pay attention to the order in if statements - because this is after the age >= 18 portion, 
# # that will be true FIRST - move this statement to the front to set it up correctly
# elif(age > 100):
#     print("You are too old to sign up")
# else:
#     print("You CANNOT sign up for a credit card")

response = input("Would you like some food? (Y/N) ")

if(response == 'Y' or response == 'y'):
    print("Have some pizza")
elif(response == 'N' or response == 'n'):
    print("Don't eat because you're not hungry")
else:
    print("Please choose a valid response (Y or N)")
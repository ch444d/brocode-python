# Logical operators = evaluate multiple conditions (and, or, not)
# or = at least one condition must be True
# and = both conditions must be true
# not = inverts the condition (not False, not True)

temp = 25
is_raining = False

# if (temp > 35 or temp < 0 or is_raining == True):
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# if(temp >= 25 and is_raining == False):
#     print("The outdoor event is still scheduled")
# else:
#     print("The outdoor event is cancelled")

if temp == 25 and not is_raining:
    print("The outdoor event is still scheduled")  
else:
    print("The outdoor event is cancelled")
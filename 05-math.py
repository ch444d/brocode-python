import math

# items = 5

#standard
# items = items + 1
# items = items - 1
# items = items * 1
# items = items / 1

#augmented operators
# items += 1
# items -= 1
# items *= 1
# items /= 1

#exponents
# items = items ** 2
# items **= 2
# remainder = items % 3 # modulus
#
# print(items)
# print(remainder)

# x = 3.14
# y = -4
# z = 5
#
# print(round(x))
# print(abs(y))
# print(pow(y, 3))
# print(max(x, y, z))
# print(min(x, y, z))
# print(math.pi)
# print(math.e) #exponential constant?
# print(math.sqrt(x))
# print(math.ceil(x))
# print(math.floor(x))

##############################################
# Print the circumference & area of a circle #
##############################################

# C = 2 * pi * r

# pi = math.pi
# r = float(input("What is the radius? "))
# C = 2 * pi * r
# A = pi * r ** 2
# # A = pi * pow(r, 2) would also be acceptable
#
# print(f"Circumference = {C} units")
# print(f"Circumference = {round(C)} units (rounded)")
# print(f"Circumference = {round(C, 2)} units (rounded to 2 digits)")
# print(f"Circumference = {round(C, 3)} units (rounded to 3 digits)")
# print(f"Circumference = {math.trunc(C)} units (truncated)")
# print("\n")
# print(f"Area = {A} units")
# print(f"Area = {round(A, 4)} units (rounded to 4 digits)")
# print(f"Area = {math.trunc(A)} units (truncated)")

##############################################
# Find the hypotenuse of a right triangle    #
##############################################

a = float(input("What is the length of side A? "))
b = float(input("What is the length of side B? "))
c = math.sqrt((a**2)+pow(b, 2)) # two ways of writing a^2 + b^2

print(f"C = {c}")
print(f"C = {round(c,2)}")
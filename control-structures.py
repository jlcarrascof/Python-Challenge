# Estructuras de control.
# if, match (switch), while, foreach, while.

# Bool
# True, False

# Operadores relacionales (==, !=, <, >, <=, >=)
# Operadores lógicos (and, or, not)

number1 = 10
number2 = 20

result = number1 == number2
print(result)

# And 

result = number1 < number2 and 10 == 10 and 5 != 5 and True and True and False
print(result)

# Or
result = number1 < number2 or 10 == 10 or 5 != 5 or True or True or False
print(result)

# Not
print(not not result)
result = True and (True and False)
print(result)
result = True and (True and (not (False and False)))
print(result)

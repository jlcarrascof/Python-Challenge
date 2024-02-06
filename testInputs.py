# Testing inputs for the program

result = input('Ingresa tu nombre: ')
print('Se ingresó por teclado: ' + result)
print(type(result))

name = input('Ingresa tu nombre: ')
age = int(input('Ingresa tu edad: '))
score = float(input('Ingresa tu calificación: '))
active = input('El usuario se encuentra activo? (si/no): ') == 'si'

print(name)
print(age)
print(score)
print(active)

# int, float, string, bool

print (type(name), type(age), type(score), type(active))

print (type(str(10)))

# Operadores relacionales (==, !=, <, >, <=, >=)
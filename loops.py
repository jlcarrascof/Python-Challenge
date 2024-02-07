# foreach y while

# foreach cuando sepamos cuantas iteraciones vamos a hacer
# while cuando no sepamos cuantas iteraciones vamos a hacer

# foreach

title = 'Estructuras de control'
for caracter in title:
    print(caracter)

for number in range(1, 101):
    if number % 2 == 0:
        print(number)

# while

number = 0
while number < 10:
    print(number)
    number += 1
else:
    print('Fin del ciclo while')

# Ejemplo: adivina el número
random, number, intentos = 5, 0, 0

while number != random and intentos < 5:
    number = int(input('Ingresa un número: '))
    intentos += 1
else:
    if number != random:
        print('Lo siento, has agotado tus intentos')
    elif number == random:
        print('Felicidades! Adivinaste el número')
        print('Número de intentos: ', intentos)

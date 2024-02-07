# Estructuras de control.
# if, match (switch), while, foreach, while.

if False:
    print('La condición se cumple')
    print('Este bloque solo se ejecuta si la condición es True')
else:
    print('Este bloque solo se ejecuta si la condición es False')

age = int (input('Ingresa tu edad: ')) # string
if age >= 0 and age <= 110:

    if age >= 18:
        print('Tienes la edad para votar.')
    else:
        print('Lo sentimos, no puedes votar')

else:
    print('>>> La edad no es válida, intenta de nuevo (min: 0, max: 110)')

color = 'blue'

if color == 'green':
    print('Puede continuar')
else:
    if color == 'yellow':
        print('Alto parcial')
    else:
        if color == 'red':
            print('Alto total')
        else:
            print('No reconozco el color')


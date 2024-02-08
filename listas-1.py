# Listas - Estructuras de Datos.

# Indices      0        1        2        3        4               5      6
courses = ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails', 'Rust', 'C#']

last_index = len(courses) - 1
index = int(input('Ingrese el indice del curso que desea ver: '))

if index <= last_index:
    print(courses[index])
else:
    print('Lo sentimos, el índice ingresado NO es válido')

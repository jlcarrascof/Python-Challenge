# Listas - Estructuras de Datos.
# append, insert, extend, remove, clear, index, count.

# Indices      0        1        2        3        4               5      6
#                                         -4       -3             -2      -1  
courses = ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails', 'Rust', 'C#']
new_courses = ['Java9', 'Docker', 'Unix']

courses.extend(new_courses)

print(courses)
print(courses[-1])

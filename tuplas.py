# Tuplas - Diccionarios.
# Llave != String - Llaves = Objetos inmutables (String, Enteros, Flotantes, Bool, Tuplas)

user = {
    'name': 'Cody',
    'age': 10,
    'email': 'info@codigofacilito.com',
    'active': True, 
}

if 'name' in user:
    print('La llave "name" existe en el diccionario')
    print(user['name'])

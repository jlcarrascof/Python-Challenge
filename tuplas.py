# Tuplas - Diccionarios.
# Llave != String - Llaves = Objetos inmutables (String, Enteros, Flotantes, Bool, Tuplas)
# keys() - values() - items()

user = {
    'name': 'Cody',
    'age': 10,
    'email': 'info@codigofacilito.com',
    'active': True, 
}

for key, value in tuple(user.items()):
    print(key, value)

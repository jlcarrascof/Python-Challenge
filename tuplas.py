# Tuplas - Diccionarios.

settings = ('localhost', 3306, 'root', 'password', 'database')

host, *_, password, database = settings

print(host, password, database)

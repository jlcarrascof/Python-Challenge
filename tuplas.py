# Tuplas - Diccionarios.

settings = ('localhost', 3306, 'root', 'password', 'database')

host, port, *_ = settings

print(host, port)

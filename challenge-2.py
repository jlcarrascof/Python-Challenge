# CodigoFacilito Challenge 2: Registro de usuarios

num_users = int(input('¿Cuántos nuevos usuarios se pretenden registrar? '))

# Itera sobre el número de usuarios a registrar
for i in range(0, num_users):
    print("Registro del usuario:", i+1)

    # Solicita y valida el nombre
    while True:
        first_name = input('Ingresa tu nombre: ')
        if 5 <= len(first_name) <= 50:
            break
        else:
            print('El nombre debe tener entre 5 y 50 caracteres.')

    # Solicita y valida los apellidos
    while True:
        last_name = input('Ingresa tus apellidos: ')
        if 5 <= len(last_name) <= 50:
            break
        else:
            print('Los apellidos deben tener entre 5 y 50 caracteres.')

    # Solicita y valida el número de teléfono
    while True:
        telephone = input('Ingresa tu número de teléfono: ')
        if len(telephone) == 10 and telephone.isdigit():
            break
        else:
            print('El número de teléfono debe tener 10 dígitos.')

    # Solicita y valida el correo electrónico
    while True:
        email = input('Ingresa tu correo electrónico: ')
        if 5 <= len(email) <= 50:
            break
        else:
            print('El correo electrónico debe tener entre 5 y 50 caracteres.')

    print('Hola ' + first_name + ' ' + last_name, ' en breve recibirás un correo a ' + email + '.')

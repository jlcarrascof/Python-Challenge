# CodigoFacilito Challenge 4: Registro de usuarios con ID usando diccionarios y opciones de menú

users = {}

while True:
    print("\nMenú:")
    print("A.- Registrar nuevos usuarios")
    print("B.- Listar usuarios")
    print("C.- Ver información de un usuario")
    print("D.- Editar información de un usuario")
    print("E.- Salir del programa")
    option = input("Elige una opción: ")

    if option.upper() == 'A':
        user_id = len(users) + 1
        print("Registro del usuario:", user_id)

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

        # Almacena la información del usuario en un diccionario
        users[user_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'telephone': telephone,
            'email': email
        }

        print('Hola ' + first_name + ' ' + last_name, ' en breve recibirás un correo a ' + email + '.')

    elif option.upper() == 'B':
        print("Los identificadores de los usuarios registrados son:", list(users.keys()))

    elif option.upper() == 'C':
        user_id = int(input("Ingresa el ID del usuario que quieres consultar: "))
        if user_id in users:
            print(users[user_id])
        else:
            print("No existe un usuario con ese ID.")

    elif option.upper() == 'D':
        user_id = int(input("Ingresa el ID del usuario que quieres editar: "))
        if user_id in users:
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

            # Actualiza la información del usuario en el diccionario
            users[user_id] = {
                'first_name': first_name,
                'last_name': last_name,
                'telephone': telephone,
                'email': email
            }

            print('La información del usuario ha sido actualizada.')
        else:
            print("No existe un usuario con ese ID.")

    elif option.upper() == 'E':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

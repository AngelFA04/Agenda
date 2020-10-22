from main import select_option

import re
NAMES = dict()


def validate_email(email):
    m = re.match(r"[\w\.-]+@.+\.[a-zA-Z]{2,5}", email)
    if(m):
        return True
    else:
        print("Email NO valido")
        return validate_email(str(input("Introducir email valido: ")))


def reestructure_data(name):
    structure = {"name":"", "phone_number": "", "email": ""}
    if name in NAMES.keys():
        structure['name'] = name
        structure['phone_number'] = NAMES.get(name)[0]
        structure['email'] = NAMES.get(name)[1]
    return structure


def print_personal_info(name):
    """ Print all user info using her name """
    info = reestructure_data(name)
    return f"{info['name']}  {info['phone_number']}\
               {info['email']}"+"\n+"+"-"*49


def print_menu():
    print("1. Agregar persona")
    print("2. Modificar persona")
    print("3. Borrar persona")
    print("4. Buscar por nombre e imprimir información")
    print("5. Leer agenda desde archivo")
    print("6. Guardar agenda en archivo")
    print("7. Salir")
    print("8 - Leer agenda actual")
    try:
        opcion = int(input("Introduce una opción: "))
        if opcion >= 1 and opcion <= 9:
            return opcion
        else:
            raise OptionOutofRange
    except:
        print("\n++++Introduce una opción valida++++\n")
        return print_menu()


def add_person(name):
    NAMES[name] = []
    # Introduce phone number
    phoneNumber = str(input(f"Introducir número de telefono de {name}: "))
    NAMES[name].append(phoneNumber)

    # Introduce email
    email = str(input(f"Introducir email de {name}: "))
    validate_email(email)

    NAMES[name].append(email)
    print('-'*7+f'\n{name} ha sido agregado a la base de datos\n'+'-'*7)


def modify_person(name):
    if name in NAMES.keys():
        new_phone = input("Ingresar nuevo número telefonico: ")
        new_email = input("Ingresar nuevo email: ")
        validate_email(new_email)

        NAMES[name][0] = new_phone
        NAMES[name][1] = new_email
        print(f"Los datos de {name} han sido modificados")
    else:
        print("\nERROR, la persona no existe\n")
        select_option()


def delete_person(name):
    if name in NAMES.keys():
        del NAMES[name]
        print('-'*7+f'\n{name} ha sido eliminado de la base de datos\n'+'-'*7)
    else:
        print("-"*7+"\nERROR, la persona no existe\n")
    select_option()


def search_by_name(name):
    if name in NAMES.keys():
        print_personal_info(name)
    else:
        print("La persona que busca no se encuentra en la base de datos")


def read_contacts():
    print("\n" + "-"*49 + "\n| Nombre \t | Telefono \t | Correo\n" + "-" * 49)
    for name in NAMES.keys():
        print(print_personal_info(name))


def names():
    return NAMES

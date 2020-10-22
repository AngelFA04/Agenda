import persistence
import functions as fun
import sys


def select_option():
    """ Function to choose an option from menu """
    opcion = fun.print_menu()

    def finish():
        yn = input("¿Desea guardar los cambios? y/n: ")
        if yn.lower() == 'y':
            # Save file in text database
            persistence.save_file(str(nameFile), fun.names())
            sys.exit()
        elif yn.lower() == 'n':
            sys.exit()
        else:
            finish()

    if opcion == 1:
        name = input("Introduce el nombre de la persona: ")
        fun.add_person(name)
    elif opcion == 2:
        name = input("Introduce el nombre de la persona: ")
        fun.modify_person(name)
    elif opcion == 3:
        name = input("Introduce el nombre de la persona: ")
        fun.delete_person(name)
    elif opcion == 4:
        name = input("Introduce el nombre de la persona: ")
        fun.search_by_name(name)
    elif opcion == 5:
        persistence.read_contacts_file(nameFile)
    elif opcion == 6:
        persistence.save_file(str(nameFile), fun.names())
    elif opcion == 7:
        yn = input("¿Desea guardar los cambios? y/n: ")
        if yn.lower() == 'y':
            # Save file in text database
            persistence.save_file(str(nameFile), fun.names())
            sys.exit()
        elif yn.lower() == 'n':
            sys.exit()
        else:
            finish()
        return True
    elif opcion == 8:
        fun.read_contacts()
    return False


if __name__ == "__main__":
    nameFile = str(input("Nombre para base de datos: ")) + ".csv"
    persistence.init_csv(nameFile)

    print("Este es un programa para almacenar una agenda,\n\
           seleccione una de las siguientes opciones:\n")

    while not select_option():
        select_option()

import csv
import os
import functions as fun


def init_csv(nameFile):
    if os.path.isfile(nameFile):
        print("La agenda ya existe, se trabajara sobre la misma agenda")
    else:
        with open(nameFile, mode='w') as csv_file:
            fieldnames = ['name', 'phone_number', 'email']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()


def save_file(nameFile, NAMES):
    with open(nameFile, mode='w') as csv_file:
        fieldnames = ['name', 'phone_number', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for person in NAMES.keys():
            p = fun.reestructure_data(person)
            writer.writerow(p)
    print("La agenda se ha guardado")


def read_contacts_file(nameFile):
    """ Reads users saved in text file """
    print("El nombre del archivo a leer es: " + nameFile)
    with open(nameFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        print("\n" + "-"*49 + "\n| Nombre \t | Telefono \t | Correo\n"
              + "-" * 49)
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                datos = f"{row[0]}  {row[1]}  {row[2]}"+"\n+"+"-"*49
                print(datos)
                line_count += 1
        print(f'Processed {line_count} lines.\n')

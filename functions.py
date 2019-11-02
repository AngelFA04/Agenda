from main import elegirOpcion
import csv

NAMES = dict()

def reestructureData(name):
    print(NAMES[name])
    structure = {"name":"", "phone":"", "email":""} 
    if name in NAMES.keys():
        structure['name'] = name
        structure['phone'] = NAMES.get(name)[0]
        structure['email'] = NAMES.get(name)[1]
    return structure

def printPersonalInfo(name):

  pass


def printMenu():
  print("1. Agregar persona")
  print("2. Modificar persona")
  print("3. Borrar persona")
  print("4. Buscar por nombre e imprimir información")
  print("5. Leer agenda")
  print("6. Guardar agenda en archivo")
  print("7. Salir")
  try:
    opcion = int(input("Introduce una opción: "))
    if opcion >= 1 and opcion <= 7:
      return opcion
    else:
      raise OptionOutofRange
  except:
    print("\n++++Introduce una opción valida++++\n")
    return printMenu()


def addPerson(name):
  NAMES[name] = []
  #Introducir telefono
  phoneNumber = str(input( f"Introducir número de telefono de {name}: "))    
  NAMES[name].append(phoneNumber)

  #Introducir correo
  email = str(input(f"Introducir email de {name}: "))
  NAMES[name].append(email)
  print('-'*7+f'\n{name} ha sido agregado a la base de datos\n'+'-'*7)

def modifyPerson(name):
  if name in NAMES.keys():  
    new_phone = input("Ingresar nuevo número telefonico: ")
    new_email = input("Ingresar nuevo email: ")
    NAMES[name][0] = new_phone
    NAMES[name][1] = new_email
  else:
    print("\nERROR, la persona no existe\n")
    elegirOpcion()


def deletePerson(name):
  if name in NAMES.keys():  
    del NAMES[name]
    print('-'*7+f'\n{name} ha sido eliminado de la base de datos\n'+'-'*7)
  else:
    print("-"*7+"\nERROR, la persona no existe\n")
    elegirOpcion()

def searchByName(name):
  if name in NAMES.keys():
    printPersonalInfo(name)
  else:
    print("La persona que busca no se encuentra en la base de datos")

def readContacts():
  pass

def names():
  return NAMES

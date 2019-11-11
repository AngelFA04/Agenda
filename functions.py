from main import elegirOpcion
import persistence as p
import csv

NAMES = dict()



def reestructureData(name):
    structure = {"name":"", "phone_number":"", "email":""} 
    if name in NAMES.keys():
        structure['name'] = name
        structure['phone_number'] = NAMES.get(name)[0]
        structure['email'] = NAMES.get(name)[1]
    return structure

#Imprimir la informacion del usuario basado en el nombre
def printPersonalInfo(name):
  info = reestructureData(name)
  #cadena = f"Nombre: {info['name']}  Número: {info['phone_number']} Email: {info['email']}"
  cadena = f"{info['name']}  {info['phone_number']}  {info['email']}"+"\n+"+"-"*49
  return cadena

def printMenu():
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
  print("\n" + "-"*49 +"\n| Nombre \t | Telefono \t | Correo\n" +"-"*49)
  for name in NAMES.keys():
    print(printPersonalInfo(name))


def names():
  return NAMES

import persistence
import functions as fun

#Función para seleccionar una opcion del menu
def elegirOpcion():
  opcion = fun.printMenu()
  def finish():
    yn = input("¿Desea guardar los cambios? y/n: ")
    if yn.lower() == 'y':
      #Guardar archivo de base de datos
      persistence.writeDictionary(str(nameFile), fun.names())
    elif yn.lower() == 'n':
      return
    else:
      finish()
      
  if opcion == 1:
    name = input("Introduce el nombre de la persona: ")
    fun.addPerson(name)
  elif opcion == 2:
    name = input("Introduce el nombre de la persona: ")
    fun.modifyPerson(name)
  elif opcion == 3:
    name = input("Introduce el nombre de la persona: ")
    fun.deletePerson(name)
  elif opcion == 4:
    name = input("Introduce el nombre de la persona: ")
    fun.searchByName()
  elif opcion == 5:
    fun.readContacts()
  elif opcion == 6:
    persistence.writeDictionary(str(nameFile), fun.names())
  elif opcion == 7:
    yn = input("¿Desea guardar los cambios? y/n: ")
    if yn.lower() == 'y':
      #Guardar archivo de base de datos
      persistence.writeDictionary(str(nameFile), fun.names())
    elif yn.lower() == 'n':
      close()
    else:
      finish()
    return True
  elif opcion == 9:
    fun.readContacts()
  return False
    
if __name__ == "__main__":
  nameFile = str(input("Nombre para base de datos: ")) + ".csv"
  persistence.initCSV(nameFile)
  
  print("Este es un programa para almacenar una agenda,\nseleccione una de las siguientes opciones:\n")
  
  while not elegirOpcion():
    elegirOpcion()
  

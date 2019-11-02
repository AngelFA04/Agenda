
import functions as fun

#Funcin para seleccionar una opcion del menu
def elegirOpcion():
  opcion = fun.printMenu()
  
  if opcion == 1:
    name = input("Introduce el nombre de la persona: ")
    fun.addPerson(name)
  elif opcion == 2:
    name = input("Introduce el nombre de la persona: ")
    fun.modifyPerson(name)
  elif opcion == 3:
    name = input("Introduce el nombre de la persona: ")
    fun.deletePerson(name)






if __name__ == "__main__":
  print("Este es un programa para almacenar una agenda,\nseleccione una de las siguientes opciones:\n")
  fun.addPerson(input("Introduce el nombre de la persona: "))
  print(fun.reestructureData("Angel"))
  elegirOpcion()
  print(fun.names())

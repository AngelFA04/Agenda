import csv
import os
import functions as fun

def initCSV(nameFile):
  
  if os.path.isfile(nameFile):
    print("El archivo existe!!!")
  else:  
    with open(nameFile, mode='w') as csv_file:
      fieldnames = ['name', 'phone_number', 'email']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      writer.writeheader()

def writeDictionary(nameFile, NAMES):
    with open(nameFile, mode='a') as csv_file:
        fieldnames = ['name', 'phone_number', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for person in NAMES.keys():
           p = fun.reestructureData(person)
           writer.writerow(p)

def saveFile(nameFile,NAMES):
    with open(nameFile, mode='w') as csv_file:
        fieldnames = ['name', 'phone_number', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for person in NAMES.keys():
           p = fun.reestructureData(person)
           writer.writerow(p) 
    
#Lee la agenda que se ha guardado en los archivos
def readContactsfile(nameFile):
  with open(nameFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        else:
            print(row)
            datos = f"{row[0]}  {row[1]}  {row[2]}"+"\n+"+"-"*49
            print(datos)
            line_count += 1
    print(f'Processed {line_count} lines.')


        


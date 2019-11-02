import csv
import os
import functions as fun

def initCSV(nameFile):
  
  if os.path.isfile(nameFile):
    print("El archivo existe!!!")
  else:  
    with open(nameFile, mode='w') as csv_file:
      fieldnames = ['name', 'number', 'email']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      writer.writeheader()

def writeDictionary(nameFile):
    with open(nameFile, mode='a') as csv_file:
        fieldnames = ['name', 'number', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        
        
def extractData():
    pass
        


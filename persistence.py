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
        
def extractData(nameFile):
    with open('employee_birthday.txt', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      line_count = 0
      for row in csv_reader:
          if line_count == 0:
              print(f'Column names are {", ".join(row)}')
              line_count += 1
              print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
              line_count += 1
              print(f'Processed {line_count} lines.')
    pass
        


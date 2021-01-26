import csv
import math
#import panda as pd

def year():
    with open('C:/Users/malej/Desktop/2NV/CN2/vehicles.csv', encoding='utf8') as f:
        document = csv.reader(f)
        for row in document:
            year = list(row[6])
            if len(year) == 0:
                print('')
            else:
                year_mof = year[0]+year[1]+year[2]+year[3]
                print(year_mof)

year() 

def regiones():
    with open('C:/Users/malej/Desktop/2NV/CN2/vehicles.csv', encoding='utf8') as f:
        document = csv.reader(f)

        nombres_regiones = []
        for row in document:
            region = row[3]
            nombres_regiones.append(region)

        cada_region = list(set(nombres_regiones))

        for re in cada_region:
           cant = nombres_regiones.count(re)
           print(re + "  " + str(cant))

regiones()
            
def registros_completos():
    with open('C:/Users/malej/Desktop/2NV/CN2/vehicles.csv', encoding='utf8') as f:
        document = csv.reader(f)

        for column in document:
            if len(column) == 0:
                print("")
            else:
                #print(column)
                if  isinstance(column, str):
                    crearDoc(column)
                else:
                    for col in column:
                        crearDoc(col)
        print("Archivo creado exitosamente")

def crearDoc(column):
    archivo = open('registros_completos.csv', 'a', encoding='utf8')
    archivo.write(column)
    archivo.close()
    

registros_completos()
    

def filtar_price_cond():
    with open('C:/Users/malej/Desktop/2NV/CN2/vehicles.csv', encoding='utf8') as f:
        document = csv.reader(f)

        index_color = []
        index_cond = []
        index_common = []
        for row in document:
            price = list(row[5])
            condicion = list(row[9])
            for row in price:
                row = int(row)
                if row >= 15000:
                    row_blue = price.index(row)
                    index_color.append(row_blue)
            for row in condicion:
                if row == "good":
                    row_exc_good = condicion.index(row)
                    index_cond(row_exc_good)
                elif row == "excellent":
                    row_exc_good = condicion.index(row)
                    index_cond(row_exc_good)
            for x in index_color:
                for y in index_cond:
                    if x == y:
                        index_common.append(x)
            
            for index in index_common:
                for i, row in enumerate(document):
                    if i == index:
                        datos = row
                        if datos[6]:
                            print(row)

filtar_price_cond()

def filtar_company_color():
    with open('C:/Users/malej/Desktop/2NV/CN2/vehicles.csv', encoding='utf8') as f:
        document = csv.reader(f)

        index_color = []
        index_company = []
        index_common = []
        for row in document:
            company = row[7]
            color = row[19]
            if color == "blue":
                row_blue = color.index(color)
                index_color.append(row_blue)
            
            for co in company:
                if co == "chevrolet":
                    row_company = company.index(co)
                    index_company.append(row_company)
                    print(index_company)
            for x in index_color:
                for y in index_company:
                    if x == y:
                        index_common.append(x)
            
            for index in index_common:
                for i, row in enumerate(document):
                    if i == index:
                        datos = row
                        if datos[6]:
                            print('')

filtar_company_color() 



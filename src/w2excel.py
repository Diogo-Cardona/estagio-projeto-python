import openpyxl
import random
import time

def make_formula(order, cell1, cell2, tipo):
    if tipo == "apenas2":
        formula = '=' + order + '(' +str(cell1) +',' +str(cell2) +')'
    if tipo == "todos":
            formula = '=' + order + '(' +str(cell1) +':' +str(cell2) +')'

    return formula

def write2excel(file, sheet, current, voltage, order3column):
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook[sheet]
    finalx = 0
    #write the values into a worksheet in a pre-existing excel file
    worksheet['A1'] ='Tensão'
    worksheet['B1'] ='Corrente'
    worksheet['C1'] ='Potência'
    for x in range(len(voltage)):
        cell1 = 'A' + str(x+2)
        cell2 = 'B'+str(x+2)
        worksheet[cell1]=voltage[x]
        worksheet[cell2]=current[x]
        formula = make_formula(order3column, cell1, cell2, "apenas2")
        cell3 = 'C'+str(x+2)
        worksheet[cell3].value = formula
        finalx = x
    worksheet['E1'] = make_formula('SUM', 'C2', 'C'+str(finalx+2), "todos")
    # worksheet['D2'] = duration
    # worksheet['E1'] ='Energia ='
    # worksheet['F1'] = make_formula('PRODUCT', 'D1', 'D2')
    workbook.save(file)
    workbook.close()

from page_objects import PageObject, PageElement
import Negativo as n
import Positivo as p
import ApiTest as t
import Data as d
import fileinput
import re
import csv
import xlrd 

d.periodo()

#print("Teste_API")
t.test_Api()


print("Testes Positivos")
loc = ("D:\\Python\\Sicredi\\DataPositivo.xlsx") 
wb = xlrd.open_workbook(loc) 
sheetp = wb.sheet_by_index(0)
sheetp.cell_value(0,0)


for i in range(sheetp.nrows):
    p.Teste_Positivo(str(sheetp.cell_value(i,0)),str(sheetp.cell_value(i,1)),str(sheetp.cell_value(i,2)),str(sheetp.cell_value(i,3)),str(sheetp.cell_value(0,4)))
    p.Teste_Positivo(str(sheetp.cell_value(i,0)),str(sheetp.cell_value(i,1)),str(sheetp.cell_value(i,2)),str(sheetp.cell_value(i,3)),str(sheetp.cell_value(1,4))

print("Fim Testes Positivos")
print("Testes Negativos")
loc = ("D:\\Python\\Sicredi\\DataNegativo.xlsx") 
wb = xlrd.open_workbook(loc) 
sheetn = wb.sheet_by_index(0)
sheetn.cell_value(0,0)
for i in range(sheetn.nrows):
    n.Teste_Negativo(str(sheetn.cell_value(0,0)),str(sheetn.cell_value(i,1)),str(sheetn.cell_value(i,2)),str(sheetn.cell_value(i,3)),str(sheetn.cell_value(0,4)))
    n.Teste_Negativo(str(sheetn.cell_value(0,0)),str(sheetn.cell_value(i,1)),str(sheetn.cell_value(i,2)),str(sheetn.cell_value(i,3)),str(sheetn.cell_value(1,4)))
    n.Teste_Negativo(str(sheetn.cell_value(1,0)),str(sheetn.cell_value(i,1)),str(sheetn.cell_value(i,2)),str(sheetn.cell_value(i,3)),str(sheetn.cell_value(0,4)))
    n.Teste_Negativo(str(sheetn.cell_value(1,0)),str(sheetn.cell_value(i,1)),str(sheetn.cell_value(i,2)),str(sheetn.cell_value(i,3)),str(sheetn.cell_value(1,4)))
print("Fim Testes Negativos")

d.periodo()

"""-----------------------------------------------------------------------------
Script Name:      List of pgtables Tool
Version:          1.1
Description:      Receives as input the .csv table which lists posgresql tables 
                  and prepares it for further processing in the .bat tool. 
Created By:       Kusasalethu Sithole
Date:             2019-08-28
Last Revision:    2019-08-29
--------------------------------------------------------------------------------"""


import csv
import openpyxl
import pandas as pd
from pandas import DataFrame

#convert csv to working xlsx
wb = openpyxl.Workbook()
ws = wb.active

with open('list_of_pgtables.csv') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        ws.append(row)

ws.insert_cols(1)
wb.save('list_of_pgtables.xlsx')


#concantenate schema name and table name columns
wb = pd.read_excel('list_of_pgtables.xlsx', header = None)
wb[1] = wb[1].str.strip()
wb[2] = wb[2].str.strip()
wb[0] = wb[1].astype(str) + '.' + wb[2].astype(str)
wb.to_excel('list_of_pgtables.xlsx', index=False)


#remove unwanted rows and columns
wb = openpyxl.load_workbook('list_of_pgtables.xlsx')
sheet = wb['Sheet1']
sheet.delete_rows(1,2)
sheet.delete_rows(1,2)
sheet.delete_cols(2,3)
sheet.delete_cols(2,3)      
wb.save('list_of_pgtables.xlsx')   
wb.close()


#convert working xlsx to final csv
wb = pd.read_excel('list_of_pgtables.xlsx')
wb.to_csv('list_of_pgtables_2.csv', index=False)



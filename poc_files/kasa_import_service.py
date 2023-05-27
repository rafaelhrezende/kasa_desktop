from kasa_lib import *
from kasa_service_connect import *
import csv

def extract_year(row):
    return row[0][0:4]

def extract_month(row):
    return row[0][7:10]

def extract_value(row):
    return row[3]

def extract_completDT(row):
    return row[6]

def extract_payDay(row):
    return row[7]

def extract_method(row):
    return row[5]

def send(bill_id, refYear, refMonth, value, method, dueDate, completionDate, payDay, status):
    print("--Sending--")
    result = KasaInvoiceService.createInvoice(bill_id,  refYear, refMonth, value, method, dueDate, completionDate, payDay, status)
    print(f"-- -- Send result: {result.success} | {result.message}")
    if result.success == False:
        print(f"- Y: '{year}'")
        print(f"- M: '{month}'")
        print(f"- Value: '{value}'")
        print(f"- Comp DT: '{completionDate}'")
        print(f"- Pay Day: '{payDay}'")
        print(f"- Method: '{method}'")
        

user = 'rafael@email.com'
password = 'P3D4jfnj*4.!'
result = KasaService.authenticate(user, password)

if result.success:
    token = result.json()['access_token']
    set_token(token)
    with open('files/File1.csv',) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print(row)
            year = extract_year(row)
            month = extract_month(row)
            value = extract_value(row)
            completionDate = extract_completDT(row)
            payDay = extract_payDay(row)
            method = extract_method(row)
            
            bill_id = -1
            send(bill_id, year, month, value, method, payDay, completionDate, payDay, 1)
else:
    print(result.message)
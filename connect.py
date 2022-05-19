import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\aquin\Downloads\Database01.accdb;')
    print("Database is Connected")


except pyodbc.Error:
    print("Error in Connection")
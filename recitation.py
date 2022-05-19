import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\aquin\Downloads\Database01.accdb;')
    print("Database is Connected")

    database = connect.cursor()

    data = (11, "Jhoriz Rodel F. Aquino", 19, "Cavite", "22/07/2002", 90)

    database.execute("INSERT INTO Table1 (ID, FullName, Age, Address, Birthdate, SemGrade) VALUES(?, ?, ?, ?, ?, ?)", data)
    database.commit()

except pyodbc.IntegrityError:
    print("Unsuccessful: record is already added -- cannot be duplicated")

except pyodbc.Error:
    print("Error in Connection")



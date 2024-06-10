import pyodbc

# Connection string for Windows Authentication
connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=Geo\\SQLEXPRESS;DATABASE=Ada_App;Trusted_Connection=yes"

try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed: ", e)

import pyodbc

# server = 'localhost,1433'
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
# connection_string = "DRIVER={ODBC Driver 17 for SQL Server};"
# connection_string += f"SERVER={server};"
# connection_string += f"DATABASE={database};"
# connection_string += f"UID={username};"
# connection_string += f"PWD={password}"
#
# docker_northwind = pyodbc.connect(connection_string)
# cursor = docker_northwind.cursor()
#
# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# print(row)

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=databases3.spartaglobal.academy;'
                      'Database=Northwind;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT @@version;')

for row in cursor:
    print(row)
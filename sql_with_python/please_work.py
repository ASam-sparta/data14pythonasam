import pyodbc

class NWProducts:
    def __init__(self):
        self.server = 'databases.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.connection_string = "DRIVER={ODBC Driver 17 for SQL Server};"
        self.connection_string += f"SERVER={self.server};"
        self.connection_string += f"DATABASE={self.database};"
        self.connection_string += f"UID={self.username};"
        self.connection_string += f"PWD={self.password}"

        self.northwind = pyodbc.connect(self.connection_string)  # This creates a connection
        self.cursor = self.northwind.cursor()  # Cursor object, used to interact with database

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def average_unit_price(self):
        records = self._sql_query("SELECT * FROM Products")
        unit_price = []
        for row in records:
            unit_price.append(row.UnitPrice)
        avg_unit_price = sum(unit_price)/len(unit_price)
        return avg_unit_price



        # # for i in range(8):
        # sum = 0
        # product = 0
        # for row in records:
        #     if row.CategoryID == 1:
        #         sum += row.UnitPrice
        #         product += 1
        #         average = sum / product
        # print(average)
        # # return


query = """
        SELECT CategoryID 
        , AVG(UnitPrice) AS AvgPrice
        FROM Products
        GROUP BY CategoryID
        """
# northwind = NWProducts()
# northwind.average_unit_price()
# northwind._sql_query(query)  # Execute the SQL command where the cursor is


# results = []
# for row in northwind.cursor:  # Dealing with one row at a time is better than pulling all in
#     # results.append(row)
#     print(row)  # Cursor
# This prints an class of row which has attributes which are the column names


if __name__ == "__main__": # If this file is imported, the name of the file changes, and therefore this code does not run
    query = """
            SELECT CategoryID 
            , AVG(UnitPrice) AS AvgPrice
            FROM Products
            GROUP BY CategoryID
            """
    nw = NWProducts
    # print(nw.average_unit_price())
    print(nw._sql_query(query))


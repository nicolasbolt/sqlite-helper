import os
from sqlitehelper import DatabaseManager

#Get the current directory that this file is in and add the database file to the end of it 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "ComicData.db")

#Pass in that path and the table name and create an instance of DatabaseManager
#The constructor of this class will attempt to create a connection and will print any error messages
dbManager = DatabaseManager(db_path, "issues")

#Pass in the column name and the search query to this function will either return the row number of the search query 
#or it will print out an error and return 0 if it can't find the value  
row = dbManager.find_row("col2", "11")

#Pass in the row number and the column to retrieve the value, it will return the value if it can find it, 
#or it will print out an error and return 0 if it can't find it
print(dbManager.find_column_data(row, "col1"))

#Commits any changes to the database and closes the connection
dbManager.close()
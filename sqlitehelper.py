import sqlite3
import pandas as pd

class DatabaseManager:

	def __init__(self, dbPath, table):
		self.dbPath = dbPath
		self.table = table
		self.table_exists = False

		try:
			self.conn = sqlite3.connect(dbPath)
			self.c = self.conn.cursor()
		except sqlite3.OperationalError as e:
			print(e)

		self.c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=(?)", (self.table,))

		if self.c.fetchone()[0]==1:
			self.table_exists = True

			self.df = pd.read_sql_query(f"SELECT * from {self.table}", self.conn)
		else:
			print("Table Does Not Exist")


	def find_row(self, col, query):
		if self.table_exists:
			
			try:
				result = self.df.loc[self.df[col] == query].index[0]
				return result
			except IndexError as e:
				print("Search Query Not Found")
		else:
			print("Table Doesn't Exist")
			return None


	def find_column_data(self, rowNum, col):
		if self.table_exists:

			try:
				result = self.df.loc[rowNum, col]
				return result
			except KeyError as e:
				print("KeyError: " + str(e))
				print("Row Number Out of Range or Column Doesn't Exist in Table")

		else:
			print("Table Doesn't Exist")
			return None


	def print_df(self):
		print(self.df)


	def close(self):
		self.conn.commit()
		self.conn.close()
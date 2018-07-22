import sqlite3

class Database(object):

	def __init__(self):
		self.connect_status = None

	def create(self):
		self.connect_status = sqlite3.connect("calc_records.sqlite3")
		self.connect_status.cursor().execute("CREATE TABLE Calculations (ID INTEGER PRIMARY KEY, QUERY TEXT);")

	def delete(self):
		self.connect_status.execute("DELETE FROM Calculations WHERE ID = 10;")

	def add(self, calculation):
		self.connect_status.execute("INSERT INTO Calculations (QUERY) VALUES (?);", calculation)

	def query(self, record):
		self.connect_status.execute("SELECT Query FROM Calculations WHERE Query = (?);", record)

	def check_size(self):
		pass

	def connect(self):
		self.connect_status = sqlite3.connect("calc_records.sqlite3")
		return self.connect_status.cursor()

	def commit(self):
		self.connect_status.commit()

	def close(self):
		self.connect_status.close()


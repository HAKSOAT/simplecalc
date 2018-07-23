import sqlite3

class Database(object):

	def __init__(self):
		self.connect_status = None
		self.cursor = None

	def create(self):
		self.connect_status = sqlite3.connect("calc_records.sqlite3")
		self.cursor = self.connect_status.cursor()
		self.cursor.execute("CREATE TABLE Calculations (Time INTEGER, Query TEXT);")

	def add(self, calculation, time):
		self.cursor.execute("INSERT INTO Calculations (Time, Query) VALUES (?, ?);", (time, calculation))

	def delete(self):
		self.cursor.execute("DELETE FROM Calculations WHERE Time = (SELECT min(Time) FROM Calculations);")

	def query(self, record):
		try:
			self.cursor.execute("SELECT Query FROM Calculations ORDER BY Time ASC;")
			return self.cursor.fetchall()[record][0]
		except IndexError:
			return ""
	def check_size(self):
		self.cursor.execute("SELECT count(Time) FROM Calculations;")
		return self.cursor.fetchone()[0]

	def connect(self):
		self.connect_status = sqlite3.connect("calc_records.sqlite3")
		self.cursor = self.connect_status.cursor()

	def commit(self):
		self.connect_status.commit()

	def close(self):
		self.connect_status.close()


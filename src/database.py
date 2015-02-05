#coding: utf8
import MySQLdb
from cfg import Config

class DB(object):
	def __init__(self,host,user,passwd,db):
		self._host = host
		self._user = user
		self._passwd = passwd
		self._db  = db

		self._conn = None
		self._cursor = None
		
	def _isconnected(self):
		return self._conn and self._cursor

	def _connect(self):
		if self._isconnected():
			return

		self._conn = MySQLdb.connect(host=self._host,user=self._user,passwd=self._passwd,db=self._db,charset='utf8') 
		self._cursor = self._conn.cursor()			
	def execute(self,*args,**kws):
		self._connect()
		self._cursor.execute(*args,**kws)
	def getall(self):
		if not self._isconnected():
			raise Exception("DB Error: Execute first")
		return self._cursor.fetchall()
	def getone(self):
		if not self._isconnected():
			raise Exception("DB Error: Execute first")
		return self._cursor.fetchone()
	def insert_id(self):
		if not self._isconnected():
			raise Exception("DB Error: Execute first")
		return self._conn.insert_id()
	def commit(self):
		if not self._isconnected():
			raise Exception("DB Error: Execute first")
		self._conn.commit()

	def close(self):
		if self._cursor: self._cursor.close()
		if self._conn:
			self._conn.close()
		self._cursor = None
		self._conn = None
	def __del__(self):
		self.close()

	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		self.close()

def withdb(func):
    def run(*args,**kws):
        cfg = Config["db"]
        db = DB(cfg["host"],cfg["user"],cfg["passwd"],cfg["db"])
        try:
            kws['db'] = db
            return func(*args,**kws)
        finally:
            db.close()
    return run

#coding: utf8
import sqlite3,os.path,time
from config import DATA_DIR

class DB(object):
	def __init__(self,filename,timeout=0):
		self.filename = filename
		self.timeout = timeout
		self.cursor = None
		self.conn = None
		self.conntime = 0
		self.reset()
	def reset(self):
		self.close()
		self.conn = sqlite3.connect(self.filename)
		self.conn.text_factory = str
		self.cursor = self.conn.cursor()
		self.conntime = int(time.time())
		#--设定一些为了性能--
		
	def reconn(self):
		if self.timeout < 1:
			return
		n = int(time.time())
		if n - self.conntime >= self.timeout:
			self.reset()
		self.conntime = n
	def execute(self,*args,**kws):
		v = list(args)
		if isinstance(v[0],str):
			v[0]=v[0].replace('%s','?')
			v[0]=v[0].replace('%d','?')
		if len(v) > 1:
			if not isinstance(v[1],list) and not isinstance(v[1],tuple):
				v[1] = (v[1],)
		args = tuple(v)
		self.reconn()
		self.cursor.execute(*args,**kws)
	def getall(self):
		self.reconn()
		return self.cursor.fetchall()
	def getone(self):
		self.reconn()
		return self.cursor.fetchone()
	def insert_id(self):
		return self.cursor.lastrowid
	def commit(self):
		self.reconn()
		self.conn.commit()
	def close(self):
		if self.cursor:
			self.cursor.close()
		if self.conn:
			self.conn.commit()
			self.conn.close()
		self.cursor = None
		self.conn = None
	def __del__(self):
		self.close()

def createDB():
	dbfile = os.path.join(DATA_DIR,'db.dat')
	if os.path.exists(dbfile):
		raise Exception("数据库文件db.dat已经存在!")
	return DB(dbfile)

def initDB():
	"""
	URLS:
		ID				int pk autoinc
		IS_HEART		int  //是否加星标
		IS_ARCHIVED		int  //是否提交了快照0:未，1：提交了 ,2: 需要提交的
		ARCHIVED_OK		int  //快照是否完成了0:未完成，1:完成了
		CATEGORY_ID		int  //类目的ID
		URL				text //收藏的URL
		SHORT_URL_ID	int  //URL的简洁ID值
		TITLE			text //类目的标题
		TAG				text //标签
		NOTES			text //备注
		TIE_TIME		text //收藏的时间(2013-01-01)这样的格式
		JOB_ID			text //COPYCAT服务的ID值
	"""
	db = createDB()
	db.execute("""CREATE TABLE URLS(ID INTEGER PRIMARY KEY AUTOINCREMENT,
				IS_HEART INTEGER,IS_ARCHIVED INTEGER,ARCHIVED_OK INTEGER,
				CATEGORY_ID INTEGER,URL TEXT,SHORT_URL_ID INTEGER,
				TITLE TEXT,TAG TEXT,NOTES TEXT,TIE_TIME TEXT,JOB_ID TEXT)""")
	#---
	#CREATE INDEX name ON URLS(ID,IS_HEART)
	#
	db.execute('CREATE INDEX copycat ON URLS(IS_ARCHIVED,ARCHIVED_OK)')
	"""
	CATEGORY:
		ID		int pk autoincr 
		TITLE	目录的标题
	"""
	db.execute('CREATE TABLE CATEGORY(ID INTEGER PRIMARY KEY AUTOINCREMENT,TITLE TEXT)')
	db.execute('INSERT INTO CATEGORY(TITLE) VALUES(%s)',"默认收藏夹")
	"""
	API:
		APP_ID : int
		SECURITY_KEY: text
		ROOT_URL : text
		VALID : int  这个设定是否有效的1:有效,0:无效
	"""
	db.execute('CREATE TABLE API(APP_ID INTEGER,SECURITY_KEY TEXT,ROOT_URL TEXT,VALID INTEGER)')
	"""
	SERVICES:
		SERVICE_ID : int(COPYCAT=1)
		ENABLED	   : int(0:未激活,1:激活)
		MSG		   : text(改变的原因)
	"""
	db.execute('CREATE TABLE SERVICES(SERVICE_ID INTEGER PRIMARY KEY,ENABLED INTEGER,MSG TEXT)')
	db.execute('INSERT INTO SERVICES(SERVICE_ID,ENABLED,MSG) VALUES(1,0,"")')
	"""
	VERSION:
		CUR	       : int 当前使用的版本
		LATEST     : int 最新的版本
		CHECKTIME  : int 上次检查的时间
		MSG		   : text 更新的内容
	"""
	db.execute('CREATE TABLE VERSION(CUR INTEGER,LATEST INTEGER,CHECKTIME INTEGER,MSG TEXT)')
	db.execute('INSERT INTO VERSION(CUR,LATEST,CHECKTIME,MSG) VALUES(1,1,0,"")')
	db.close()

if __name__=="__main__":
	initDB()

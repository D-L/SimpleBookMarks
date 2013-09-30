#!/usr/bin/env python2
#coding: utf8
from threading import Thread
import os.path

from utils import getDB,getCC,wait,now
from copycat import ccError
import urllib2,json

from archive import needarchive,archiveapiok,ARCHIVED_DIR

def checkversion(db):
	#检查是否有新版本了
	db.execute('SELECT CUR FROM VERSION')
	cur, = db.getone()
	#---Call to ---
	checkurl = 'https://www.youaitie.net/personal/version/'
	data = urllib2.urlopen(checkurl,timeout=5).read()
	obj = json.loads(data)
	ver = int(obj['version'])
	if cur < ver:
		db.execute('UPDATE VERSION SET LATEST=%s,MSG=%s',(ver,obj['msg'].encode('utf8')))
	db.execute('UPDATE VERSION SET CHECKTIME=%s',now())
	db.commit()

def submit(db):
	#1. 是否Enable,2.是否API设定好了
	if not needarchive(db) or not archiveapiok(db):
		return

	cc = getCC(db)
	db.execute('SELECT ID,URL FROM URLS WHERE IS_ARCHIVED=2')

	done = []
	for aid,url in db.getall():
		try:
			jobid = cc.snap(url)
			done.append( (aid,jobid) )
		except Exception,msg:
			if isinstance(msg,ccError):
				if msg.msgid == 100: #没有余额了
					db.execute('UPDATE SERVICES SET MSG=%s,ENABLED=0 WHERE SERVICE_ID=1',"服务余额不足，自动停用。请充值,然后启用服务!")
					db.commit()
			break
	if done:
		for aid,jobid in done:
			db.execute('UPDATE URLS SET IS_ARCHIVED=1,JOB_ID=%s WHERE ID=%s',(jobid,aid))
		db.commit()

def getdata(db):
	if not archiveapiok(db):
		return

	cc= getCC(db)
	db.execute('SELECT ID,JOB_ID FROM URLS WHERE IS_ARCHIVED=1 AND ARCHIVED_OK = 0')

	done = []
	for aid,jobid in db.getall():
		try:
			if cc.isfinished(jobid):
				#去获取结果了
				name = os.path.join(ARCHIVED_DIR,"%s.dat" % aid)
				cc.get2file(jobid,name)
				done.append( aid )
		except Exception,msg:
			pass
	if done:
		for aid in done:
			db.execute('UPDATE URLS SET ARCHIVED_OK=1 WHERE ID=%s',aid)
		db.commit()

class Checker(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.daemon = True
	def run(self):
		db = getDB()

		db.execute('SELECT CHECKTIME FROM VERSION')
		vt, = db.getone()
		while True:
			#--开始检查--
			#1. 先检查已经提交的是否完成了(这个在前面)
			try:
				getdata(db)
			except Exception,msg:
				print msg
			#2. 检查是否有需要提交的
			try:
				submit(db)
			except Exception,msg:
				print msg
			#3. 检查新版本
			if now() - vt > 1000*3600*12: #1天检查2次
				try:
					checkversion(db)
					vt = now()
				except Exception,msg:
					print msg
			wait(30000)

def runchecker():
	check = Checker()
	check.start()
	return check

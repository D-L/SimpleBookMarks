#!/usr/bin/env python2
#coding: utf8

import sys,os.path,shutil,os,zipfile,json
sys.path.append("..")

from database import withdb
from utils import utf8
from cfg import Config

from recorder import Recorder

from token import TOKEN

def getone(recorder,jobid,id):
	tmpfile = os.path.join(Config["datadir"],"%s.zip" % id)
	if os.path.exists(tmpfile):
		os.remove(tmpfile)

	recorder.get2file(jobid,tmpfile)

	fd = zipfile.ZipFile(tmpfile)
	#将title抽取出来
	v = json.loads( fd.read('meta.json') )
	fd.close()

	return utf8(v['title'])

@withdb
def submit(db):
	recorder = Recorder(TOKEN)
	db.execute('SELECT ID,RECORD_ID FROM TASK WHERE STATUS=1 AND APPROVED=1 AND ENABLED=1')

	done = []
	for id,jobid in db.getall():
		try:
			if recorder.isfinished(jobid):
				#获取结果
				title = getone(recorder,jobid,id)
				done.append( (id,title ))
		except Exception,msg:
			print msg

	for id,title in done:
		db.execute('UPDATE TASK SET STATUS=2,TITLE=%s WHERE ID=%s',(title,id))
	db.commit()

if __name__=="__main__":
	import time
	while True:
		try:
			submit()
		except Exception,msg:
			print msg
		time.sleep(300)

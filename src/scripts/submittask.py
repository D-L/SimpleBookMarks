#!/usr/bin/env python2
#coding: utf8

import sys
sys.path.append("..")

from database import withdb
from utils import utf8

from recorder import Recorder
from token import TOKEN

@withdb
def submit(db):
	recorder = Recorder(TOKEN)
	db.execute('SELECT ID,URL FROM TASK WHERE STATUS=0 AND APPROVED=1 AND ENABLED=1')

	done = []
	for id,url in db.getall():
		try:
			jobid = recorder.record(utf8(url))
			done.append( (id,jobid) )
		except Exception,msg:
			print msg
	for id,jobid in done:
		db.execute('UPDATE TASK SET STATUS=1,RECORD_ID=%s WHERE ID=%s',(jobid,id))
	db.commit()

if __name__=="__main__":
	submit()

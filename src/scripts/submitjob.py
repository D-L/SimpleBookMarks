#!/usr/bin/env python2
#coding: utf8

import sys
sys.path.append("..")

from datetime import date
from database import withdb
from utils import urlkey,utf8

@withdb
def submit(db):
	db.execute('SELECT ID,URL,UK,SECONDS,now()-SUBMIT_TIME FROM JOB WHERE VALID=1')

	todo = []
	for id,url,uk,second,diff in db.getall():
		if diff < second:
			continue
		todo.append( (id,utf8(url),uk) )

 	n = date.today()
	month = "%s%02d" % (n.year,n.month)
	day   = "%s%02d%02d" % (n.year,n.month,n.day)
	for id,url,uk in todo:
		db.execute('INSERT INTO TASK(URL,UK,TITLE,MONTH_ID,DAY_ID,STATUS,APPROVED,ENABLED,CREATE_TIME) VALUES(%s,%s,"",%s,%s,0,1,1,now())',(url,uk,month,day))
		db.execute('UPDATE JOB SET SUBMIT_TIME=now() WHERE ID=%s',(id,))
		print "Submit",url,"OK"
	db.commit()

if __name__=="__main__":
	submit()

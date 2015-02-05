#!/usr/bin/env python2
#coding: utf8

import sys
sys.path.append("..")


from database import withdb
from utils import urlkey,utf8

@withdb
def add(url,seconds,db):
	uk = urlkey(url)
	db.execute('SELECT URL,SECONDS,SUBMIT_TIME FROM JOB WHERE VALID=1 AND UK=%s',(uk,))
	for url,second,st in db.getall():
		u = utf8(url)
		if u == url:
			print "Already:",u," Second:",second," Submit_Time:",str(st)
			return
	#-
	db.execute('INSERT INTO JOB(URL,UK,SUBMIT_TIME,SECONDS,VALID) VALUES(%s,%s,"2014-01-01",%s,1)',(url,uk,seconds))
	db.commit()
	print "Add OK"

if __name__=="__main__":
	if len(sys.argv) != 3:
		print "Usage:",sys.argv[0],"URL Interval"
		print "Interval:"
		print "        ...m ->分"
		print "        ...h ->小时"
		print "        ...d ->天"
		sys.exit(0)

	interval = sys.argv[2]
	d = interval[-1]
	ss = int(interval[:-1])
	if d == 'm':
		ss *= 60
	elif d == 'h':
		ss *= 3600
	elif d == 'd':
		ss *= 3600*24
	else:
		print "invalid interval"
		sys.exit(0)

	if ss < 1:
		print "invalid interval"
		sys.exit(0)
		
	add(sys.argv[1],ss)

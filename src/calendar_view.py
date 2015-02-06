#!/usr/bin/env python2
#coding:utf-8

import os,hashlib,os.path
from bottle import run,template,static_file,redirect,request,route,response,post,get,abort,static_file
from database import withdb
from datetime import date,timedelta
import calendar

from cfg import Config
from utils import utf8,urlkey
from readzipone import readone

@get('/css/<filename>')
def css(filename):
    return static_file(filename, root='static/css/')

@get('/fonts/<filename>')
def font(filename):
    return static_file(filename, root='static/fonts/')

@get('/js/<filename>')
def js(filename):
    return static_file(filename, root='static/js/')

def onemonth(db,year,month):
	prevmonth = '/'
	if year >= 2014:
		if month > 1:
			prevmonth = '/month/%s%02d/' % (year,month-1)
		else:
			prevmonth = '/month/%s12/' % (year-1)

 	n = date.today()
	curyear,curmonth = n.year,n.month

	nextmonth = '/'
	if year >= 2014:
		if (year < n.year) or (year == n.year and month < n.month):
			if month > 11:
				nextmonth = '/month/%s01/' % (year+1)
			else:
				nextmonth = '/month/%s%02d/' % (year,month+1)
		
	db.execute('SELECT DISTINCT DAY_ID FROM TASK WHERE MONTH_ID=%s%02d AND APPROVED=1 AND ENABLED=1 AND STATUS=2' % (year,month))
	exists = set()
	for i, in db.getall():
		exists.add(i)

	i,days = calendar.monthrange(year,month)

	firstweek = [None]*49
	for x in xrange(days):
		v = int('%s%02d%02d' % (year,month,x+1))
		if v in exists:
			firstweek[i+x] = ('/day/%02d/' % v,'%02d' % (x+1))
		else:
			firstweek[i+x] = ('','%02d' % (x+1))

	weeks = []
	for x in xrange(7):
		t = firstweek[x*7:x*7+7]
		if filter(None,t): weeks.append(t)

	return template('month',title="%s年%02d月" % (year,month),weeks=weeks,prev=prevmonth,next=nextmonth)

@get("/")
@withdb
def home(db):
 	n = date.today()
	return onemonth(db,n.year,n.month)

@get("/month/<monthid:re:\d+>/")
@withdb
def month(monthid,db):
	if len(monthid) != 6:
		abort(404,"NO Found")
	return onemonth(db,int(monthid[:4]),int(monthid[4:]))

@get('/day/<dayid:re:\d+>/')
@withdb
def oneday(dayid,db):
	counts = {} #url :count
	data = {}
	db.execute('SELECT ID,URL,TITLE,CREATE_TIME FROM TASK WHERE DAY_ID=%s AND APPROVED=1 AND ENABLED=1 AND STATUS=2',(dayid,))
	for taskid,url,title,ct in db.getall():
		url,title = utf8(url),utf8(title)
		ct = ('%s' % ct).split()[1]

		if url in data:
			data[url].append( (taskid,title,ct) )
			counts[url]+= 1
		else:
			data[url] = [ (taskid,title,ct) ]
			counts[url] = 1

	v = [ (counts[url],url,t) for url,t in data.iteritems() ]
	v.sort(reverse=True)
		
	return template('day',dayid=dayid,data=v)

@get('/url/')
@withdb
def oneurl(db):
	turl = request.GET.get('url','')
	if not turl:
		abort(404,"NO FOUND")

	try:
		dayid = int(request.GET.get('day','0'))
	except:
		abort(404,"NO FOUND")

	data = []
	if dayid == 0:
		uk = urlkey(turl)
		db.execute('SELECT ID,URL,TITLE,CREATE_TIME FROM TASK WHERE UK=%s AND APPROVED=1 AND ENABLED=1 AND STATUS=2 LIMIT 100',(uk,))
	else:
		db.execute('SELECT ID,URL,TITLE,CREATE_TIME FROM TASK WHERE DAY_ID=%s AND APPROVED=1 AND ENABLED=1 AND STATUS=2',(dayid,))
	for taskid,url,title,ct in db.getall():
		url,title = utf8(url),utf8(title)
		if url != turl:
			continue
		
		data.append( (taskid,title,ct) )

	if not data:	
		abort(404,"NO FOUND")

	return template('url',dayid=dayid,url=url,title=data[0][1],data=data)

@get("/page/<taskid:re:\d+>/")
@withdb
def page(taskid,db):
	return onepage(db,taskid,"index.html")

@get("/page/<taskid:re:\d+>/<name:re:.+>")
@withdb
def pageone(taskid,name,db):
	return onepage(db,taskid,name)

def onepage(db,taskid,name):
	db.execute('SELECT count(0) FROM TASK WHERE ID=%s AND APPROVED=1 AND ENABLED=1 AND STATUS=2',(taskid,))
	cc, = db.getone()
	if cc < 1: 
		abort(404,"NO FOUND")

	return readone(taskid,name)

@get("/everyday/")
@withdb
def everyday(db):
	data = []
	db.execute('SELECT URL,SUBMIT_TIME FROM JOB WHERE VALID=1 ORDER BY ID DESC')
	for url,st in db.getall():
		data.append( (utf8(url),"%s" % st) )

	return template("everyday",urls=data)

@get("/ifound/")
def ifound():
	return template("ifound")

@post("/newworld/")
@withdb
def newworld(db):
	url = request.POST.get('url','')
	comment = request.POST.get('comment','')

	if url and comment == Config['newworldkey']:
		uk = urlkey(url)
		n = date.today()
		month = '%s%02d' % (n.year,n.month)
		day  = '%s%02d' % (month,n.day)

		db.execute('INSERT INTO TASK(URL,UK,TITLE,MONTH_ID,DAY_ID,STATUS,APPROVED,ENABLED,CREATE_TIME) VALUES(%s,%s,"",%s,%s,0,1,1,now())',(url,uk,month,day))
		db.commit()

	homepage= request.urlparts[1].split(':')[0]
	return template("thanks",homepage=homepage)

run(host="127.0.0.1",port=Config["port"], server="tornado")

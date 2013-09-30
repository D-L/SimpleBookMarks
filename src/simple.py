#!/usr/bin/env python2
#coding: utf8
from bottle import get,run,redirect,template,error,request,static_file,TornadoServer
from utils import wrapdb,compressit
from checker import runchecker
import os.path

import heart
import bookmarks
import info
import tie
import category
import archive
import urls

from config import STATIC_DIR

def errorone(error):
	if error.body:
		return template('error',msg=error.body)
	return template('error',msg='')

@error(401)
def error401(error): return errorone(error)
@error(404)
def error404(error): return errorone(error)
	
@get('/<kind:re:css|js|font|img>/<filename:re:.*>')
def allkind(kind,filename):
	return static_file(filename,root=os.path.join(STATIC_DIR,kind))

@get('/<filename:re:.*html>')
def html(filename):
	return static_file(filename,root=os.path.join(STATIC_DIR,"html"))

@get("/favicon.ico")
def favicon():
	return static_file("favicon.ico",root=STATIC_DIR)

@get("/")
@wrapdb
def homepage(db):
	db.execute('SELECT COUNT(0) FROM URLS')
	urlcount, = db.getone()
	if int(urlcount) > 0:
		redirect('/my/',302)
	else:
		return compressit(template("welcome"))

@get("/tools/")
def tools():
	httpdomain = 'http://'+request.urlparts.netloc
	return compressit(template("tools",httpdomain=httpdomain))

def runweb():
	#从外界获取配置
	host=''
	port=0
	for line in open("config.txt","rb"):
		content = line.strip().lower()
		if content.find('host=') >=0:
			host=content.replace('host=','').strip()
		elif content.find('port=') >=0:
			port =int(content.replace('port=','').strip())

	run(host=host,port=port,server=TornadoServer)

if __name__=="__main__":
	checker = runchecker()
	runweb()

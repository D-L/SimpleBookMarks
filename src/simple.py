#!/usr/bin/env python2
#coding: utf8
from bottle import get,run,redirect,template,error,static_file,TornadoServer
from database import updatedb
from utils import wrapdb,compressit,CFG,login
from checker import runchecker
import os.path

import heart
import bookmarks
import info
import tie
import category
import archive
import urls
import user

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
@login
@wrapdb
def homepage(db):
	db.execute('SELECT COUNT(0) FROM URLS')
	urlcount, = db.getone()
	if int(urlcount) > 0:
		redirect('/my/',302)
	else:
		return compressit(template("welcome"))

@get("/tools/")
@login
def tools():
	return compressit(template("tools",httpdomain=CFG.domain))

@get("/sysupdate/")
@wrapdb
def sysupdate(db):
	updatedb(db)
	return "升级成功!"

def runweb():
	#从外界获取配置
	run(host=CFG.host,port=CFG.port,server=TornadoServer)

if __name__=="__main__":
	checker = runchecker()
	runweb()

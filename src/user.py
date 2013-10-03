#coding: utf8
from bottle import get,post,request,template,redirect,response
from utils import wrapdb,now,md5sum,CFG,login
import random,urlparse,datetime

@post("/signin/")
@wrapdb
def signin(db):
	"""
		登陆
	"""
	passwd = request.POST.get('passwd','')
	db.execute('SELECT PASSWD FROM USER')
	v, = db.getone()
	if v != passwd:
		return template("error",msg="密码错误")
	#-设定cookie
	token = md5sum('%s-%s' % (now(),random.random()*now()))
	db.execute('INSERT INTO COOKIE(TOKEN) VALUES(%s)',token)
	d = urlparse.urlparse(CFG.domain).netloc.split(':')[0]
	response.set_cookie('token',token,path="/",expires=int(now()/1000)+3600*24*365,domain=d)
	redirect("/",301)

@get("/signout/")
@login
@wrapdb
def signout(db):
	token = request.get_cookie('token','')
	db.execute('DELETE FROM COOKIE WHERE TOKEN=%s',token)
	redirect("/",301)

@post("/0.1/password/")
@login
@wrapdb
def password(db):
	#新的密码
	cur = request.POST.get('cur','')
	n = request.POST.get('new','')
	if not cur or not n:
		return {"error":"密码不能不填吧"}
	db.execute('SELECT PASSWD FROM USER')
	v, = db.getone()
	if v != cur:
		return {"error":"密码不对"}
	db.execute('DELETE FROM USER')
	db.execute('INSERT INTO USER(PASSWD) VALUES(%s)',n)
	return {"ok":"密码成功更新"}

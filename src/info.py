#coding: utf8

from bottle import get,post,request,redirect,template
from utils import wrapdb

@get("/info/")
@wrapdb
def info(db):
	enabled = False
	msg = ''
	db.execute('SELECT ENABLED,MSG FROM SERVICES WHERE SERVICE_ID = 1')
	v = db.getone()
	if v:
		msg = v[1]
		enabled = v[0] == 1
	db.execute('SELECT APP_ID,SECURITY_KEY,ROOT_URL FROM API WHERE VALID = 1')
	v = db.getone()
	if not v:
		appinfo = None
	else:
		appid,key,url = v
		appinfo = (int(appid),key,url)
	return template('info',appinfo=appinfo,enabled=enabled,msg=msg)

@post("/setcopycat/")
@wrapdb
def setcopycat(db):
	appid = request.POST.get('appid','').strip()
	key = request.POST.get('key','').strip()
	root = request.POST.get('rooturl','').strip()
	if not appid or not key or not root:
		return template('error',msg='设置参数不能为空啊')

	try:
		appid = int(appid)
	except:
		return template('error',msg='APPID 应该是个数字吧？')
	db.execute('UPDATE API SET VALID=0')
	db.execute('INSERT INTO API(APP_ID,SECURITY_KEY,ROOT_URL,VALID) VALUES(%s,%s,%s,1)',(appid,key,root))
	db.commit()
	redirect('/info/',302)

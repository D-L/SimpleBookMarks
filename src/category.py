#coding: utf8

from bottle import get,post,template,request
from utils import wrapdb,ulen
from dbutils import getCategory

@post("/0.1/delcat/")
@wrapdb
def apidelcat(db):
	"""
		API接口的删除某个类目.
	"""
	catid = request.POST.get('category','').strip()
	try:
		catid = int(catid)
	except:
		return {'error':'您要删除那个收藏夹？'}

	db.execute('SELECT 1 FROM CATEGORY WHERE ID=%s',catid)
	v = db.getone()
	if not v:
		return {'error' : '此收藏夹已删除'}
	#==检查这个收藏夹底下是否还有书签==
	db.execute('SELECT 1 FROM URLS WHERE CATEGORY_ID=%s LIMIT 1',catid)
	v = db.getone()
	if v:
		return {'error' : '此收藏夹内还有收藏的有爱帖'}

	db.execute('DELETE FROM CATEGORY WHERE ID=%s',catid)
	db.commit()
	return {'ok':1}

@post("/0.1/newcat/")
@wrapdb
def apinewcat(db):
	"""
		api的新建目录
	"""
	title = request.POST.get('title','').strip()
	if not title: return {'error' : '收藏夹的名称总是不可少的'}
	if ulen(title) > 128: return {'error' : '收藏夹的名称太长了'}

	curid = 0
	ret = getCategory(db)
	for cid,t in ret:
		if t.lower() == title.lower():
			break
		curid += 1
	if curid == len(ret): #没有相同的
		db.execute('INSERT INTO CATEGORY(TITLE) VALUES(%s)',title)
		db.commit()
		ret = getCategory(db)
	else:
		ret[curid],ret[0] = ret[0],ret[curid]

	return {'content' : [ (cid,t) for cid,t in ret]}

@get("/newcategory/")
def newcategory():
	"""
		JS插件的新建链接.
	"""
	return template('newcategory')

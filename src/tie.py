#coding: utf8
import os.path
import urlparse,urllib2

from bottle import get,post,request,response,template
from utils import wrapdb,ulen,ulenget,isdeny,refineTag,html_escape,getshorturlid,normaliseurl,utf8,nt,getCC,CFG,login
from dbutils import getCategory,getdefaultcatid
from archive import needarchive,archiveapiok

from config import VIEWS_DIR 
png_1x1 = open(os.path.join(VIEWS_DIR,'1x1.png')).read()
png_10x1 = open(os.path.join(VIEWS_DIR,'10x1.png')).read()

@get("/njs/")
@login
@wrapdb
def njs(db):
	"""
		新的JS模版.
		未登陆的返回一个错误的Token好了。
		这样用户选择的时候会出现需要登陆的提示。
		模版:
			{{tags}},{{categorys}}
		输入:
			url,title
	"""
	existed = False
	lasttime = ''
	tips = ''
	url = request.GET.get('url','') #可以用来进行判断预分配的,暂时还没用上
	if url:
		cleanurl = normaliseurl(url)
		shortid = getshorturlid(url)
		db.execute('SELECT URL,TIE_TIME FROM URLS WHERE SHORT_URL_ID=%s',(shortid))
		for url,tietime in db.getall(): #怕不同URL得到相同的SHORT_URL_ID
			u = normaliseurl(url)
			if u == cleanurl:
				existed = True
				lasttime = tietime
				break
	cats = []
	for cid,title in getCategory(db):
		cats.append('<option value="%s">%s</option>' % (cid,html_escape(title)))
	#@todo: 尝试去获取最可能的Categorys和Tags.
	ret = template('jsp',tags="",categorys=''.join(cats),httpdomain=CFG.domain,existed=existed,lasttime=lasttime,tips=tips)
	response['Content-Type'] = 'application/javascript'
	return ret

@get("/jstie/")
@login
@wrapdb
def jstie(db):
	"""
		新版本的Tie过程
	"""
	url = request.GET.get('url','').strip()
	title = request.GET.get('title','').strip()
	tag = request.GET.get('tag','').strip()
	catid = int(request.GET.get('category','').strip())
	notes = request.GET.get('notes','').strip()
	isheart = request.GET.get('heart','').strip()

	if not url or isdeny(url):
		#返回1x1的数据，表示正确,实为吞没
		response['Content-Type'] = 'image/png'
		return png_1x1

	if ulen(url) > 1024: url = ulenget(url,1024)
	if ulen(title) > 1024: title=ulenget(title,1024)
	if tag:
		tag = refineTag(tag)
		if ulen(tag) > 1024: tag = ulenget(tag,1024)
	if ulen(notes) > 1024: notes= ulenget(notes,1024)

	try:
		catid = int(catid)
		#检查这个catid是否存在
		db.execute('SELECT ID FROM CATEGORY WHERE ID=%s',catid)
		v = db.getone()
		if not v: raise Exception("invalid catid param") #非法用户插入,选用默认的结果.
	except:
		catid = getdefaultcatid(db)

	heart = 0
	if isheart: heart = 1
	shortid = 0
	if url:
		shortid = getshorturlid(url)

	db.execute('INSERT INTO URLS(IS_HEART,IS_ARCHIVED,ARCHIVED_OK,CATEGORY_ID,URL,SHORT_URL_ID,TITLE,TAG,NOTES,TIE_TIME) VALUES(%s,0,0,%s,%s,%s,%s,%s,%s,%s)',(heart,catid,url,shortid,title,tag,notes,nt()))
	recordid = db.insert_id()

	if needarchive(db) and archiveapiok(db) and url:
		db.execute('UPDATE URLS SET IS_ARCHIVED=2 WHERE ID=%s',recordid)

	db.commit()
	response['Content-Type'] = 'image/png'
	return png_1x1

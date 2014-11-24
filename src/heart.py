#coding: utf8
"""
	喜爱的操作
"""
import urllib,re

from bottle import post,get,request,template
from utils import wrapdb,refineTag,login
from dbutils import getUrls,getCategory

@post("/0.1/heart/")
@login
@wrapdb
def apiheart(db):
	"""
		喜爱/取消喜爱
	"""
	bb = []
	try:
		flag = int(request.POST.get('flag','0'))
		if flag not in [0,1]:
			return {'error':'参数错误'}

		bids = request.POST.get('bookmarkids','').split(',')
		if len(bids) < 1:
			return {'error':'参数错误'}
		for b in bids:
			bid = int(b)
			if bid < 1: return {'error':'参数错误'}
			bb.append(bid)
	except:
		return {'error':'参数错误'}

	for bid in bb:
		db.execute('UPDATE URLS SET IS_HEART =%s WHERE ID=%s',(flag,bid))
	db.commit()
	return {'ok':1}

@get("/myheart/")
@login
@wrapdb
def myheart(db):
	"""
		列出全部含有心的收藏,同时可以进行编辑了.
	"""
	def buildtagurl(cid,tag):
		url = '/my/'
		v = []
		if cid:
			v.append('cid=%s' % cid)
		if tag:
			v.append('tag=%s' % urllib.quote(tag))
		if v:
			return url+'?'+'&'.join(v)
		return url

	data = []
	alltags = set()
	for urlid,cid,url,title,tags,notes,pt,thisarchive,isheart in getUrls(db):
		for x in tags:
			alltags.add('"%s"' % x.replace('"','\\"'))
		
		if isheart !=1 : continue

		thistags = []
		for t in tags:
			thistags.append( (t,buildtagurl(0,t)) ) #全局的Tag

		data.append( (urlid,url,title,cid,tags,notes,pt,thistags,isheart,thisarchive) )

	allcats = dict([ (cid,title) for cid,title in getCategory(db) ])
	ret = template('myheart',allcategorys = allcats,bookmarks=data,tags=','.join(list(alltags)),count=len(data))
	return ret
